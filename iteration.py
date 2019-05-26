def factorial(n):
	if n < 0:
		raise ValueError

	x = 1
	for i in range(1, n+1):
		x *= i
	return x


def hailstones(n):
	if n < 1:
		raise ValueError

	seq = [n]

	while n != 1:
		if n % 2 == 0:
			n = n // 2
		else:
			n = 3*n + 1
		seq.append(n)

	return seq


def fibonacci(n):
	if n < 0:
		raise ValueError

	if n == 0:
		return 0
	if n == 1:
		return 1

	# `a` and `b` represent the two most recent Fibonacci numbers calculated.
	a = 0  # 0th Fibonacci number
	b = 1  # 1st Fibonacci number

	i = 2
	# Calculate the ith Fibonacci number.
	while True:
		c = a + b
		if i == n:
			# The nth Fibonacci number was just calculated, so return it.
			return c

		# Set `a` and `b` to be the two most recent Fibonacci numbers.
		a = b
		b = c

		i += 1
