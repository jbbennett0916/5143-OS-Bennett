#EVERYTHING THAT IS IMPLIMENTED IS WORKING 
#The only thing that you have to do is add the things where
#things like CPU and IO wait time are incrimented 
#and hen the turnaround time is calculated inside the term QUEUE

from cpu import Cpu
from ioClass import IO
from jobs import Job
from new import New
from ready import Ready
from terminated import Terminated
from waiting import Waiting

def preStage():
	algo = input('Please enter and algorithm')
	timeSlice = input("Please enter a time slice")
	cpus = input("Please enter the number of CPUs")
	ios = input("Please enter the number of IO devises")
	test(algo, timeSlice, cpus, ios)

#going to have to change 'rr'
#to a variable that has the current algo that needs to be run 
def test(algo, timeSlice, cpus, ios):
	count = 0
	cpuList = []
	ioList = []

	for i in range(cpus):
		cpu = Cpu(algo, timeSlice)
		cpuList.append(cpu)

	for i in range(ios):
		io = IO()
		ioList.append(io)

	#probably not gonna pass it a time slice since he didn't specify that we needed
	#one I'm just gonna hard code in a time slice of 5 or maybe play around with
	#different numbers and see what I get 
	

	#io = IO()
	#cpu = Cpu(algo, timeSlice)

	aa = [0,1,0,6,1,6]

	jobList = []
	for i in range(1, 51):
		job = Job(aa)
		job.id = i
		jobList.append(job)

	job1 = Job([0,1,0,6,1,6])
	job2 = Job([0,2,0,6,1,4])
	newQueue = New()
	ready = Ready()
	terminated = Terminated()
	waiting = Waiting()
	
	while len(terminated.termQueue) < 30:

		if len(ready.readyQueue) > 0:
			ready.cpuWait()
		if len(waiting.waitQueue) > 0:
			waiting.ioWait()

		#move to the terminated Queue
		for i in cpuList:
			if i.term == True:
				terminated.addTerm(i.move)
				i.term = False
				print('Moved TO TERM! Count:' + str(count))

		#from IO to ready
		for i in ioList:
			if i.send == True:
				ready.addReady(i.move, 'rr')
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
				ready.addReady([i.move], 'rr')
				i.moveReady = False
				i.moving = False
				i.move = None
				i.currentTime = 0
				print('From CPU TO READY QUEUE! COUNT:' + str(count))

		#Run IO
		for i in ioList:
			if i.busy == True and i.job != None:
				i.run()
				print('Running IO! Count:' + str(count))

		
		#Run CPU
		for i in cpuList:
			if i.busy == True and i.job != None:
				i.run()
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
			ready.addReady(newQueue.queue, 'rr')
			newQueue.queue = []
			print('Added to Ready Queue! Count:' + str(count))

		#From jobslist to NewQueue
		if count == 0:
			#newQueue.addNew(job1)
			#newQueue.addNew(job2)
			for i in jobList:
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

test('rr', 5, 4,4)
