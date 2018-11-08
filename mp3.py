class Job(object):
	def __init__(self, job_stream_num, time, job_size):
		self.job_stream_num = job_stream_num
		self.time = time
		self.job_size = job_size
	
def readJobFile():
	with open("jobs.in", "r") as ins:
		arr = []
		jobs = []
		for line in ins:
			arr.append(line)
			separated = line.split(';')
			job = Job(separated[0], separated[1], separated[2])
			jobs.append(job)

	return jobs



def main():
	print("Hello World!")
	jobs = readJobFile()
	for job in jobs:
		print(job.job_stream_num)

if __name__ == '__main__':
	main()