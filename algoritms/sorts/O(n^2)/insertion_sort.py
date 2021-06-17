# Algorithms and Data Structures
# Insertion sort
# Complexity T(n) =  (n(n-2))
#                     '''2'''
# The Final complexity is
#            T(n) = \Theta(n^2)
# Best case is
#            T(n) = \Theta(n)

def insertion_sort(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j - 1] > A[j]:
            A[j],A[j - 1] = A[j - 1],A[j]
            j = j - 1
    return A

print(insertion_sort([0]))