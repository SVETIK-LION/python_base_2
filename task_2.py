"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""


def prime_factors(n):
    prim_fac = []
    i = 2
    while i <= n:
        if n % i == 0:
            prim_fac.append(i)
            n //= i
            i = 2
        else:
            i += 1

    return prim_fac


print(prime_factors(24))
