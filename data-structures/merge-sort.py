"""
# program for implementation of MergeSort

Assumption.
# assumption is to be made that left and right array that are to be merged are already sorted, which holds true.

Usually uses two functions.
# First- to divide the array virtually by tracking its start and end position
# second- it merges the left and right parts (virtual parts), into the original array in sorted way.
"""

# Merges two subarrays of arr[].
# First subarray is arr[low..mid]
# Second subarray is arr[mid+1..high]

# after the array is sorted/divided in merge_sort(), array with minimum length of 2, that is 1 in left and 1 in right, is sent here
def merge(arr, low, mid, high):
	n1 = mid - low + 1
	n2 = high - mid

	# create temp arrays 
	leftTemp = [0] * (n1)
	rightTemp = [0] * (n2)

	# Copy data to temp arrays L[] and R[] 
	for i in range(0 , n1):
		leftTemp[i] = arr[low + i]

	for j in range(0 , n2):
		rightTemp[j] = arr[mid + 1 + j]

	# Merge the temp arrays back into arr[l..r] 
	i = 0	 # Initial index of first subarray 
	j = 0	 # Initial index of second subarray 
	k = low	 # Initial index of merged subarray 

	while i < n1 and j < n2 :
		if leftTemp[i] <= rightTemp[j]:
			arr[k] = leftTemp[i]
			i += 1
		else:
			arr[k] = rightTemp[j]
			j += 1
		k += 1

	# Copy the remaining elements of leftTemp[], if there 
	# are any 
	while i < n1:
		arr[k] = leftTemp[i]
		i += 1
		k += 1

	# Copy the remaining elements of rightTemp[], if there 
	# are any 
	while j < n2:
		arr[k] = rightTemp[j]
		j += 1
		k += 1

# the function divides the array recursively untill len(arr) > 1
def mergeSort(arr, low, high):
	if low < high:
		# Same as (low+high)//2, but avoids overflow for large low and high
		mid = (low+(high-1))//2
		
		print("low: {} | mid: {} | high: {} ".format(low,mid,high))

		# Sort first and second halves 
		mergeSort(arr, low, mid)
		mergeSort(arr, mid+1, high)

		# merge array with at least 2 elements
		merge(arr, low, mid, high)


def main():
	# Test code

	arr = [12, 11, 13]
	length = len(arr)

	print ("Given array is")
	for i in range(length):
		print ("%d" %arr[i])

	mergeSort(arr, 0, length-1)

	print ("\n\nSorted array is")
	for i in range(length):
		print ("%d" %arr[i])

if __name__ == '__main__':
	main()