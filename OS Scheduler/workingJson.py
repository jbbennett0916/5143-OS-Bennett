import json

jobs = []

f = open('datafile.json')

file = json.load(f)

for i in file['jobs']:
	jobs.append(i)

values = []

for i in jobs[0]:
	values.append(i)


job = []

for i in values:
	job.append(jobs[0][i])


print(values)

print(job)

print(job[0])

#from here you would say like 
#job[0] = Arival time 
#job[1] = id
#3 = priority 
#4 = cpu bursts
#5 = ioBursts


'''
This explains how to adjust the file name and params from the command line 
I guess you do this first and then do your program???
IDK I guess I'll ask Doctor Griffin on slack and or zoom

Usage: (All params have defaults, but can be changed with the following): 

	nj      	: Number of jobs[1 - n]
	minCpuBT 	: Min cpu burst length.  Usually single digits: [1 - 9]
	maxCpuBT 	: Max cpu burst length. Whatever you want: [number larger than minCpuBT]
	minIOBT 	: Min io burst length. Usually single digits: [1 - 9]
	maxIOBT 	: Max io burst length. Whatever you want: [number larger that minIOBT]
	minNumBursts 	: Min number of bursts [1 - n]
	maxNumBursts 	: Max number of bursts [number larger than minNumBursts
	intBurstType 	: Generate bursts based on cpu intensive or io intensive [cpu,io]
	minat       	: Min jobs per arrival time [1-n]
	maxat       	: Max jobs per arrival time [number larger than minat
	minp       	: Min priority [1-n]
	maxp       	: Max priority [larger than minp]
	prioWeights 	: Priority weights [even,low,high]
	ofile       	: Outfile Name will write the output to that file.

Example Commands:

	gen_input.py ofile=filename.wut nj=N minCpuBT=N maxCpuBT=N minIOBT=N maxIOBT=N minNumBursts=N 
	maxNumBursts=N minat=N maxat=N minp=N maxp=N prioWeights=[even,high,low]
or

	gen_input.py ofile=filename.wut nj=N minCpuBT=N maxCpuBT=N minIOBT=N maxIOBT=N intBurstType=[cpu,io] 
	minat=N maxat=N minp=N maxp=N prioWeights=[even,high,low]
or

	generate_input.py prioWeights=low intensiveBurstType=cpu ofile=datafile_cpu_intense.dat
or

	generate_input.py prioWeights=high intensiveBurstType=io ofile=datafile_io_intense.dat
'''
