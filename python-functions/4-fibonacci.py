#!/usr/bin/python3
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(1, n - 1):
            fib_sequence.append(fib_sequence[i] + fib_sequence[i - 1])
        return fib_sequence
