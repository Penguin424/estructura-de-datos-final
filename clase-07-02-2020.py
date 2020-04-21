import numpy as np
import matplotlib.pyplot as plt

def fibo(num):
    if num <= 1:
        return num
    else:
        return fibo(num - 1) + fibo(num - 2)

for i in range(7):
    print(fibo(i))


def fib(n):
    a = 1
    b = 0
    for i in range(n):
        a, b = b, a + b
    return b

def fi(n):
    return fib(n) / fib(n - 1)