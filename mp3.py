import copy
from copy import deepcopy

class Job(object):
	def __init__(self, job_stream_num, time, job_size):
		self.job_stream_num = job_stream_num
		self.time = time
		self.job_size = job_size

class Block(object):
	def __init__(self, num, size):
		self.num = num
		self.size = size
		self.assigned_job = None

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

def read_block_file():
	with open("memory.in", "r") as ins:
		arr = []
		blocks = []
		for line in ins:
			arr.append(line)
			separated = line.split(';')
			block = Block(int(separated[0]), int(separated[1]))
			blocks.append(block)

	return blocks

def first_fit(jobs, blocks):
	print("First Fit Placement")
	print("------------------------------------")
	accumulated_time = 0
	job_completed_count = 0
	while (True):
		for block in blocks:
			if (block.assigned_job is None):
				# traverse job list and select first job from the top
				for job in jobs:
					if (job.job_size <= block.size):
						block.assigned_job = job
						print ("Job " + str(job.job_stream_num) + " is allocated in Partition #" + str(block.num))
						jobs.remove(job)
						job_completed_count += 1
						break
			else:
				# check how many ms left
				if (block.assigned_job.time == 0):
					# change
					for job in jobs:
						if (job.job_size <= block.size):
							block.assigned_job = job
							print ("Job " + str(job.job_stream_num) + " is allocated in Partition #" + str(block.num))
							jobs.remove(job)
							job_completed_count += 1
							break

		# decrement 1 ms
		for block in blocks:
			if (block.assigned_job.time > 0):
				print(block.num, block.assigned_job.time)
				block.assigned_job.time -= 1
			accumulated_time += 1
		# print("len of jobs: " + str(len(jobs)))
		# print(blocks_are_free(blocks))
		if (len(jobs) == 0):
			if (blocks_are_free(blocks)):
				break
		else:
			# check if there are blocks big enough for the jobs
			print("len: " + str(len(jobs)))
			if (not (check_blocks_can_fit(jobs, blocks))):
				print("hi")
				break

	# set to None
	for block in blocks:
		block.assigned_job.time = 0
		block.assigned_job = None


	print("\nJobs are processed in " + str(accumulated_time) + " ms.")
	print("Jobs completed: " + str(job_completed_count))
	print("Jobs that are not partitioned:")
	for job in jobs:
		print("Job " + str(job.job_stream_num))
	print("Throughput: " + str(job_completed_count / float(accumulated_time)) + " ms.")
	print("------------------------------------")

def best_fit(jobs, blocks):
	print("Best Fit Placement")
	print("------------------------------------")
	accumulated_time = 0
	job_completed_count = 0
	least_space_wasted_index = 0
	unused_partitions = []
	while (True):
		for block in blocks:
			print(str(block.num))
			if (block.assigned_job is None):
				# traverse job list and and check for best fitting block
				print("None")
				for job in jobs:
					if (job.job_size <= block.size):
						unused_partition = block.size - job.job_size
						unused_partitions.append(unused_partition)

			else:
				print("something")

				

	print("\nJobs are processed in " + str(accumulated_time) + " ms.")
	print("Jobs completed: " + str(job_completed_count))
	print("Jobs that are not partitioned:")
	for job in jobs:
		print("Job " + str(job.job_stream_num))
	# print("Throughput: " + str(job_completed_count / float(accumulated_time)) + " ms.")
	print("------------------------------------")

def blocks_are_free(blocks):
	val = False
	for block in blocks:
		if (block.assigned_job is None):
			val = True
	return val

def check_blocks_can_fit(jobs, blocks):
	val = False
	for block in blocks:
		for job in jobs:
			if (job.job_size <= block.size):
				# print("hi" + str(job.job_size))
				val = True
	return val

def main():
	print("Hello World!")
	jobs = read_job_file()
	blocks = read_block_file()
	jobs_copy = copy.copy(jobs)
	blocks_copy = copy.copy(blocks)
	for job in jobs:
		print(job.job_stream_num, job.time, job.job_size)
	for block in blocks:
		print(block.num, block.size)
	first_fit(jobs_copy, blocks_copy)
	jobs_copy2 = copy.copy(jobs)
	blocks_copy2 = copy.copy(blocks)
	blocks_copy2.sort(key=lambda x: x.size)
	first_fit(jobs_copy2, blocks_copy2)
	# best_fit(jobs_copy2, blocks_copy2)

if __name__ == '__main__':
	main()