def merge(arr, low, mid, high):
	# print("\n+++++IN MERGE+++++\n")
	# print("low: {} | mid: {} | high: {}".format(low, mid, high))

	sizeLeft = mid - low + 1
	sizeRight = high - mid
	# print("sizeLeft: {} | sizeRight: {}".format(sizeLeft, sizeRight))

	# for x in range(mid+1):
	# 	print(arr[x])
	# for x in range(mid+1, high+1):
	# 	print(arr[x])

	leftTemp = arr[low:mid+1]
	rightTemp = arr[mid+1:high+1]

	# print("leftTemp")
	# for num in leftTemp:
	# 	print(num)

	# print("rightTemp")
	# for num in leftTemp:
	# 	print(num)


	i=j=0
	k=low

	while(i < sizeLeft and j < sizeRight):
		if leftTemp[i] <= rightTemp[j]:
			arr[k] = leftTemp[i]
			i += 1
		else:
			arr[k] = rightTemp[j]
			j += 1
		k += 1

	while i < sizeLeft:
		arr[k] = leftTemp[i]
		i += 1
		k += 1

	while j < sizeRight:
		arr[k] = rightTemp[j]
		j += 1
		k += 1

def mergeSort(arr, low, high):
	if low < high:
		mid  = (low+high)//2

		# left
		# print(" Before leftSort low: {} | mid: {} | high: {}".format(low, mid, high))
		mergeSort(arr, low, mid)

		# right
		# print(" Before rightSort low: {} | mid: {} | high: {}".format(low, mid, high))
		mergeSort(arr, mid+1, high)

		# merge
		merge(arr, low, mid, high)

def main():
	a1 = [11, 20, 12, 11]

	for a in a1:
		print(a)

	mergeSort(a1, 0, len(a1)-1)
	
	print("Sorted")
	for a in a1:
		print(a)


if __name__ == '__main__':
	main()