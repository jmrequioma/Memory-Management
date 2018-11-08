class Job:
	def __init__(self, kind):
		self.kind = kind

	def whatKind(self):
		return self.kind
def main():
	print("Hello World!")
	count = Job("count")
	read = Job("read")
	print(read.whatKind())

if __name__ == '__main__':
	main()