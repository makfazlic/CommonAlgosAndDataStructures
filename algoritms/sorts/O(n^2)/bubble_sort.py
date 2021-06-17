# Algorithms and Data Structures
# Bubble sort
# Complexity T(n) =  (n(n-2))
#                     '''2'''
# The Final complexity is
#            T(n) = \Theta(n^2)
# Best case is
#            T(n) = \Theta(n^2)

def bubble_sort(A):
    for i in range(len(A)):
        j = len(A) - 1
        while j > i:
            if A[j - 1] > A[j]:
                A[j-1],A[j] = A[j],A[j-1]
            j = j - 1
    return A

print(bubble_sort([0,5,2,3,1,9,8]))