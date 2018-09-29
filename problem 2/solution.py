def solution():
	return sum([fib for fib in fib_limit(4E6) if fib % 2 == 0])


def fib_limit(limit):
	# This function will yield fibonacci upto below a limit
	numbers = []
	prev, current = 0, 1
	while current < limit:
		numbers.append(current)
		prev, current = current, current + prev
	return numbers

print(solution())



