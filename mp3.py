class Job(object):
	def __init__(self, job_stream_num, time, job_size):
		self.job_stream_num = job_stream_num
		self.time = time
		self.job_size = job_size

class Block(object):
	def __init__(self, num, size):
		self.num = num
		self.size = size
		assigned_job = None

def read_job_file():
	with open("jobs.in", "r") as ins:
		arr = []
		jobs = []
		for line in ins:
			arr.append(line)
			separated = line.split(';')
			job = Job(int(separated[0]), int(separated[1]), int(separated[2]))
			jobs.append(job)

	return jobs

def read_memory_file():
	with open("memory.in", "r") as ins:
		arr = []
		memorys = []
		for line in ins:
			arr.append(line)
			separated = line.split(';')
			block = Block(int(separated[0]), int(separated[1]))
			memorys.append(block)

	return memorys

def first_fit(jobs, memorys):
	print("First Fit Placement")
	print("------------------------------------")
	accumulated_time = 0
	job_completed_count = 0
	no_more_avlble = False
	for i in range(len(memorys)):
		for job in jobs:
			if (job.job_size <= memorys[i].size):
				accumulated_time += job.time
				job_completed_count += 1
				print ("Job " + str(job.job_stream_num) + " allocated in Partition #" + str(memorys[i].num))
				memorys[i].assigned_job = job   # put job in block
				jobs.remove(job)
				break
			# print("i value: " + str(i))
		if (i == len(memorys) - 1):   # if all partitions are occupied, check again for available
			# decrement by 1 ms all jobs in memorys
			for memory in memorys:
				memory.assigned_job.time -= 1
			i = 0

	print("Jobs are processed in " + str(accumulated_time) + " ms.")
	print("------------------------------------")

def main():
	print("Hello World!")
	jobs = read_job_file()
	memorys = read_memory_file()
	for job in jobs:
		print(job.job_stream_num, job.time, job.job_size)
	for memory in memorys:
		print(memory.num, memory.size)
	first_fit(jobs, memorys)

if __name__ == '__main__':
	main()