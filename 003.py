"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
def largest_fact():
    max_prime = 0
    thresh = num

    for i in range(1,(num+1)):
        if (i>thresh):
            break
        if is_factor(i) and is_prime(i):
            max_prime = i
            thresh = num/i
    return max_prime
def is_factor(i):
    return num%i == 0
def is_prime(i):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count += 1
    return count == 2
num = 600851475143
print(largest_fact())
