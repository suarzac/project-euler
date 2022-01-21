"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

prime_start, to_factor = 2, 600851475143
while (prime_start*prime_start <= to_factor):
	if (to_factor%prime_start == 0):
		to_factor /= prime_start
	else:
		prime_start += 2
print(to_factor)
