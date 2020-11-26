"""
Linked list in  python

# methods
 len()
 print_ll()
 get_element(position)
 append(new_element)
 insert(position, new_element)
 delete(value)
"""

class Element(object):
	def __init__(self, value=None):
		self.value = value
		self.next = None

class LinkedList(object):
	def __init__(self, head = None):
		self.head = head

	def len(self):
		"""
		returns the length of linked list
		"""
		counter = 0
		if self.head:
			current = self.head
			while current:
				counter += 1
				current = current.next
		return counter

	def print_ll(self):
		"""
		print the linked list in form 
		[e1]  [e2]  [e3]  ...
		"""
		if self.head:
			current = self.head
			while current:
				print("[{}]".format(current.value), end="  ")
				current = current.next
			print("")
		else:
			print('No elements yet!')

	def get_element(self, position):
		current_pos = 1
		if self.head:
			current = self.head
			while current and current_pos <= position:
				if current_pos == position:
					return current
				current = current.next
				current_pos += 1


	def append(self, new_element):
		"""
		add new_element to the end of the linked list
		"""
		if self.head:
			current = self.head
			while current.next:
				current = current.next
			current.next = new_element
		else:
			self.head = new_element

	def insert(self, position, new_element):
		"""
		insert the new_element at position, where the position should be in range(1, len(ll))
		"""
		current_pos = 1
		current = self.head
		if position > 1:
			while current and current_pos < position:
				if current_pos == position-1:
					new_element.next = current.next
					current.next = new_element
					return;
				else:
					current = current.next
					current_pos += 1
		elif position == 1:
			new_element.next = current
			self.head = new_element

	def delete(self, value):
		"""
		delete the element having value
		"""
		if self.head:
			previous = None
			current = self.head
			while current.value!=value and current.next:
				previous = current
				current = current.next
			if current.value == value:
				if previous:
					previous.next = current.next
				else:
					self.head = current.next

def main():
	# Test cases
	e1 = Element(1)
	e2 = Element(2)
	e3 = Element(3)
	e4 = Element(4)
	e5 = Element(5)

	ll = LinkedList(e1)
	# should print [1]
	ll.print_ll()

	ll.append(e2)
	# should print [1] [2]
	ll.print_ll()

	ll.insert(1, e3)
	# should print [3] [1] [2]
	ll.print_ll()

	# length is 3
	print("length is {}".format(ll.len()))

	ll.delete(2)
	# [3]  [1]
	ll.print_ll()

	ll.append(e4)
	ll.append(e5)

	# [3]  [1]  [4]  [5]
	ll.print_ll()

	temp = ll.get_element(3)
	# 4
	print(temp.value)

if __name__ == '__main__':
	main()