"""
QuickSort implementation in python

TIME COMPLEXITY
	Best case: nlog(n)
		# in case partition is always in the middle

	Worst case: n^2  
		# in case if an array is already sorted, be it ascending or descending
		# if pivot is picked from leftmost or rightmost

	Rectification for worst case:
		# always select middle element or any random element as pivot

SPACE COMPLEXITY
	log(n) to n: uses a stack to store recursive functions

# quicksort works on the idea that, an element in an array is said to be sorted if the elements on its left are smaller than it and elements on the right are larger than it. It really doesn't matter for this element whether those elements are in sorted order or not...

video reference: https://youtu.be/7h1s2SojIRw
"""

from swap import swap

def partition(arr, low, high):
	# this is low as pivot algorithm, by default we pich the leftmost elements as pivot

	pivot = arr[low]

	# variable i traverses from left to right
	# variable [i] is used to keep track of the elements greater than [pivot]
	i = low + 1

	# variable j traverses from right to left
	# variable [j] tracks the elements smaller than pivot
	j = high

	while(i < j):

		while(i < high and arr[i] <= pivot):
			i += 1

		while(j > 0 and arr[j] > pivot):
			j -= 1

		if(i < j):
			arr[i], arr[j] = swap(arr[i], arr[j])


	arr[low], arr[j] = swap(arr[low], arr[j])
	# j has to be postion of the pivot

	print("for PIVOT {} INDEX j is {}".format(pivot, j))
	for i in range(low, high+1):
		print(arr[i], end=" ")
	print("\n")

	return j

def quickSort(arr, low, high):
	if low < high:

		# place the pivot at proper position and return index of pivot
		pivot = partition(arr, low, high)

		# sorting the elements on the left of pivot
		quickSort(arr, low, pivot-1)

		# sorting the elements on the right of pivot
		quickSort(arr, pivot+1, high)


def main():
	a1 = [12, 20, 1, 5, 8, 12, 12, 12, 12, 20, 1, 5, 5, 5]

	# for a in a1:
	# 	print(a)
	# print("*"*8)
	quickSort(a1, 0, len(a1)-1)

	# print("+"*8 + "Final result" + "+"*8)
	# for a in a1:
	# 	print(a)

if __name__ == '__main__':
	main()