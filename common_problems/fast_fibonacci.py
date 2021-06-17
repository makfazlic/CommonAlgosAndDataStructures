# Algorithms and Data Structures
# Itterative Fibonacci sequence
# Complexity (pre-calculation) T(n) = 6 + 6(n − 1) = 6n
# Final complexity T(n) = n

def fast_fibonacci(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        prev_prev_element = 0
        prev_element = 1
        for i in range(2, n+1):
            current_element = prev_prev_element + prev_element
            prev_prev_element = prev_element
            prev_element = current_element
    return current_element

print(fast_fibonacci(5),fast_fibonacci(6),fast_fibonacci(7))