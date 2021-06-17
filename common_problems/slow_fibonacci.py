# Algorithms and Data Structures
# Recursive Fibonacci sequence
# Complexity (pre-calculation) T(n) = T (n − 1) + T (n − 2) + 3
# Final complexity T(n) >= (√2)^n =#= (1.4)^n

def slow_fibonacci(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return slow_fibonacci(n-2) + slow_fibonacci(n-1)

print(slow_fibonacci(40))