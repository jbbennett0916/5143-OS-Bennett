import json

from cpu import Cpu
from ioClass import IO
from jobs import Job
from new import New
from ready import Ready
from terminated import Terminated
from waiting import Waiting

def createJobs():

	jobList = []

	jobs = []

	f = open('datafile.json')

	file = json.load(f)

	for i in file['jobs']:
		jobs.append(i)

	#print(jobs)

	values = []

	for i in jobs[0]:
		values.append(i)

	for i in range(len(jobs)):
		aJob = []
		for x in values:
			aJob.append(jobs[i][x])
		job = Job(aJob)
		jobList.append(job)

	algo = input('Which algorithm are you using: ')
	if algo == 'rr':
		timeSlice = input("Enter your desired timeSlice: ")
		timeSlice = int(timeSlice)
	else:
		timeSlice = 5
	cpus = input('Enter the number of CPUs you wish to use: ')
	cpus = int(cpus)

	ios = input('Enter the number of IOs you wish to use: ')
	ios = int(cpus)

	test(algo, timeSlice, cpus, ios, jobList)


def test(algo, timeSlice, cpus, ios, jobs):
	count = 0
	cpuList = []
	ioList = []
	cpuActive = 0
	ioActive = 0

	for i in range(cpus):
		cpu = Cpu(algo, timeSlice)
		cpuList.append(cpu)

	for i in range(ios):
		io = IO()
		ioList.append(io)

	newQueue = New()
	ready = Ready()
	terminated = Terminated()
	waiting = Waiting()
	
	while len(terminated.termQueue) < len(jobs):

		if len(ready.readyQueue) > 0:
			ready.cpuWait()
		if len(waiting.waitQueue) > 0:
			waiting.ioWait()

		#move to the terminated Queue
		for i in cpuList:
			if i.term == True:
				terminated.addTerm(i.move, count) #added new param to calc turanaround time
				i.term = False
				print('Moved TO TERM! Count:' + str(count))

		#from IO to ready
		for i in ioList:
			if i.send == True:
				ready.addReady(i.move, algo)
				i.send = False
				i.move = None
				print('FROM IO TO READY QUEUE! Count:' + str(count))


		#Move from CPU to waiting Queue
		for i in cpuList:
			if i.moving == True and i.moveReady == False:
				waiting.addWaiting(i.move)
				i.moving = False
				i.move = None
				i.currentTime = 0
				print('FROM CPU TO WAITING QUEUE! COUNT:' + str(count))

		#Move From CPU to Ready Queue
		for i in cpuList:
			if i.moving == True and i.moveReady == True:
				ready.addReady([i.move], algo)
				i.moveReady = False
				i.moving = False
				i.move = None
				i.currentTime = 0
				print('From CPU TO READY QUEUE! COUNT:' + str(count))

		#Run IO
		for i in ioList:
			if i.busy == True and i.job != None:
				i.run()
				ioActive +=1
				print('Running IO! Count:' + str(count))

		
		#Run CPU
		for i in cpuList:
			if i.busy == True and i.job != None:
				i.run()
				cpuActive +=1
				print('Running CPU! Count:' + str(count))
		

		#from waiting to IO
		for i in ioList:
			if waiting.send == True and i.busy == False and i.pause == False:
				i.recieve(waiting.sendIo())
				if waiting.move != None:
					print('FROM WAITING QUEUE TO IO! COUNT:' + str(count))


		#from ready to CPU
		for i in cpuList:
			if ready.send == True and i.busy == False and i.pause == False:
				i.recieve(ready.sendCpu())
				if ready.move != None:
					print('FROM Ready QUEUE TO CPU! COUNT:' + str(count))


		#From new to Ready
		if len(newQueue.queue) > 0:
			ready.addReady(newQueue.queue, algo)
			newQueue.queue = []
			print('Added to Ready Queue! Count:' + str(count))

		#From jobslist to NewQueue
		if count <= len(jobs):
			for i in jobs:
				if count == i.arrival:
					newQueue.addNew(i)
					print('Added to New Queue! Count:' + str(count))


		waiting.change()

		ready.change()

		if algo == 'pb':
			if len(ready.readyQueue) > 1:
				ready.pb()
		for i in cpuList:
			i.reset()
		for i in ioList:
			i.reset()
		count += 1

	averageCpuWait = 0
	averageIoWait = 0
	averageTat = 0
	cpuActive = (cpuActive/int(cpus))/count
	ioActive = ioActive/(int(ios))/count
	for i in terminated.termQueue:
		averageIoWait += i.IOWaitTime
		averageCpuWait += i.CPUWaitTime
		averageTat += i.TurnAroundTime
	averageCpuWait /= len(jobs)
	averageIoWait /= len(jobs)
	averageTat /= len(jobs)

	print("The average CPU wait time is:" + str(averageIoWait))
	print("The average IO wait time is:" + str(averageCpuWait))
	print("The average turn around time is:" + str(averageTat))
	print("The percentage of CPU utiization is:" + str(cpuActive * 100))
	print("The percentage of I/O utiization is:" + str(ioActive * 100))
if __name__ == "__main__":
	createJobs()