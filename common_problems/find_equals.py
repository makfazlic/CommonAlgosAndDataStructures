# Algorithms and Data Structures
# Finding two equal numbers in a list
# Complexity T(n) = C (n(n-2))
#                     '''2''''

def find_equals(A):
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] == A[j]:
                return True
    return False

print(find_equals([1,2,3,4,5,6,7]))

