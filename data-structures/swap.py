"""
works as pass-by-reference in python
"""
def swap(n1, n2):
	return (n2, n1)

def main():
	a1 = 9
	a2 = 7

	a1, a2 = swap(a1, a2)
	print("a1: {} | a2: {}".format(a1, a2))

if __name__ == '__main__':
	main()