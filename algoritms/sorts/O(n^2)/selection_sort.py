# Algorithms and Data Structures
# Selection sort
# Complexity T(n) =  (n(n-2))
#                     '''2'''
# The Final complexity is
#            T(n) = \Theta(n^2)
# Best case is
#            T(n) = \Theta(n^2)

def selection_sort(A):
    length_of_A = len(A)
    for i in range(length_of_A - 1):
        smallest = i
        for j in range(i+1, length_of_A):
            if A[j] < A[smallest]:
                smallest = j
        A[i],A[smallest] = A[smallest],A[i]
    return A

print(selection_sort([1,2,4,78,5,9,1]))