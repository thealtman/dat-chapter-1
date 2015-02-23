# Fibonacci sequence
def sum_even_fibA(n):
    sumfib = 0
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        if b % 2 == 0:
            sumfib = sumfib + b
    return sumfib
 
print(sum_even_fibA(4000000))