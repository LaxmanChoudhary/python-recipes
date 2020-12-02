"""
bubble sort -a naive approach

Better approach than given
PSEUDO CODE:

do
	swapped = false
	for i = 1 to indexOfLastUnsortedElement - 1
		if leftElement > rightElement
			swap(leftElement, rightElement)
			swapped = true
while swapped

# variable [swapped] is used to keep track if the array has been sorted.
"""
from swap import swap

def bubble_sort(input_array):
	length = len(input_array)
	for i in range(length):
		for j in range(length-i-1):
			if(input_array[j] > input_array[j+1]):
				input_array[j], input_array[j+1] = swap(input_array[j], input_array[j+1])
	return input_array

def main():
	a1 = [2, 8, 6, 10, 1, 30, 20, 15, 1]
	print(bubble_sort(a1))

if __name__ == '__main__':
	main()