def solution():
	number = 600851475143
	return largest_factor(number)

def largest_factor(number):
	if number == 1: return 1
	factor = 2
	while number % factor != 0:
		factor = factor + 1
	return max(factor, largest_factor(number / factor))

print(solution())
