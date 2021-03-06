"""
binary search,
 for sorted sequences
"""
def binary_search(input_array, value):
	low = 0
	high = len(input_array) - 1
	while(low < high):
		mid = (low+high)//2
		if(input_array[mid] == value):
			return mid
		elif(value < input_array[mid]):
			high = mid
		else:
			low = mid + 1
	return -1

def main():
	test_list = [1,3,9,11,15,19,29]
	test_val1 = 25
	test_val2 = 15
	print(binary_search(test_list, test_val1))
	print(binary_search(test_list, test_val2))
	print(binary_search(test_list, 11))

if __name__ == '__main__':
	main()