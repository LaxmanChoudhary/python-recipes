"""
linked list in python
 24 Nov 2020
"""

class Element(object):
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def append(self, new_element):
		if self.head:
			current = self.head
			while current.next:
				current = current.next
			current.next = new_element
		else:
			self.head = new_element

	def insert(self, new_element, position):
		"""Insert a new node at the given position.
		Assume the first position is "1".
		Inserting at position 3 means between the 2nd and 3rd elements."""
		current_pos = 1
		if self.head:
			current = self.head
			if position == 1:
				new_element.next = current
				self.head = new_element
			while current:
				if position == current_pos+1:
					new_element.next = current.next
					current.next = new_element
					return;
				else:
					current = current.next
					current_pos += 1
		else:
			self.head = new_element

	"""
	# other one

	def insert(self, new_element, position):
	  counter = 1
	  current = self.head
	  if position > 1:
	      while current and counter < position:
	          if counter == position - 1:
	              new_element.next = current.next
	              current.next = new_element
	          current = current.next
	          counter += 1
	  elif position == 1:
	      new_element.next = self.head
	      self.head = new_element
	"""

	def get_position(self, position):
		"""Get an element from a particular position. Assume the first position is '1'. Return "None" if position is not in the list."""
		current_pos = 0

		if position != 0:
			if self.head:
				current = self.head
				current_pos += 1
				# print('head pos: {} | current.value: {}'.format(current_pos, current.value))
				while current:
					# print('current_pos: {} | current.value: {}'.format(current_pos, current.value))
					if position == current_pos:
						return current
					current = current.next
					current_pos += 1
				return None
			else:
				return None
		return None

	"""
	# other one

	def get_position(self, position):
	  counter = 1
	  current = self.head
	  if position < 1:
	    return None
	  while current and counter <= position:
			if counter == position:
	      return current
	    current = current.next
	    counter += 1
	  return None
	"""

	def display_list(self):
		current = self.head
		if self.head:
			print('head-> [{}]  '.format(current.value), end="")
			while current.next:
				current = current.next
				print('[{}]  '.format(current.value), end="")
			print("")
		else:
			print('You need to insert first!')

	def delete(self, value):
		"""Delete the first node with a given value."""
		if self.head:
			current = self.head
			if current.value == value:
				self.head = current.next
				while current.next:
					if current.next.value == value:
						current.next = current.next.next
					else:
						current = current.next

	"""
	# other one

	def delete(self, value):
	  current = self.head
	  previous = None
	  while current.value != value and current.next:
	      previous = current
	      current = current.next
	  if current.value == value:
	      if previous:
	          previous.next = current.next
	      else:
	          self.head = current.next
	"""

def main():
	# Test cases
	# Set up some Elements
	e1 = Element(1)
	e2 = Element(2)
	e3 = Element(3)
	e4 = Element(4)

	# Start setting up a LinkedList
	ll = LinkedList(e1)
	ll.append(e2)
	ll.append(e3)

	ll.display_list()
	# Test get_position
	# Should print 3
	print(ll.head.next.next.value)
	# Should also print 3
	print(ll.get_position(3).value)

	# Test insert
	ll.insert(e4,3)
	ll.display_list()
	# ll.display_list()
	# Should print 4 now
	print(ll.get_position(3).value)

	# Test delete
	ll.delete(1)
	ll.display_list()
	# Should print 2 now
	print(ll.get_position(1).value)
	# Should print 4 now
	print(ll.get_position(2).value)
	# Should print 3 now
	print(ll.get_position(3).value)

if __name__ == '__main__':
	main()