"""
Recursion
# 1. exit condition
		- return <something>
# 2. call to itself
"""

# factorial with recursion

def factorial(n):
	if(n == 1):
		return 1
	return n*factorial(n-1)


# fibonacci sequence

def fibonacci(n):
	if(n == 1):
		return 1

	if(n == 0):
		return 0

	"""
	if n == 0 or n == 1:
		return position
	"""

	return fibonacci(n-1) + fibonacci(n-2)

def main():
	print(factorial(5))
	print(fibonacci(20))

if __name__ == '__main__':
	main()