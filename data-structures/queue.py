"""
queue using list
 26 Nov 2020
"""
class Queue(object):
	def __init__(self, head=None):
		self.storage = [head]

	def enqueue(self, new_element):
		self.storage.append(new_element)

	def peek(self):
		if len(self.storage):
			return self.storage[0]

	def dequeue(self):
		if len(self.storage):
			return self.storage.pop(0)

def main():
	# setup
	q = Queue(1)
	q.enqueue(2)
	q.enqueue(3)

	# Test peek
	# 1
	print(q.peek())

	# 1
	print(q.dequeue())

	q.enqueue(4)

	# 2
	print(q.dequeue())
	
	# 3
	print(q.dequeue())
	
	# 4
	print(q.dequeue())

	q.enqueue(5)

	# 5
	print(q.peek())

if __name__ == '__main__':
	main()