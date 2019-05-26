def hailstones(n):
	if n < 1:
		raise ValueError
    if n == 1:
        return [1]

    if n % 2 == 0:
        return [n] + hailstones(n//2)
    else:
        return [n] + hailstones(3*n + 1)
