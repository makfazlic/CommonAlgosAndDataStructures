# Merging of two arrays using Merge Sort
# Complexity T(n) = O(nlog(n))

def merge(A, B):
    i = 0
    j = 0
    X = []
    while i < len(A) or j < len(B):
        if i < len(A) and (j >= len(B) or A[i] < B[j]):
            X.append(A[i])
            i += 1
        else:
            X.append(B[j])
            j += 1
    return X

def merge_sort(A):
    if len(A) == 1:
        return A
    middle = len(A) // 2
    left = merge_sort(A[:middle])
    right = merge_sort(A[middle:])
    return merge(left, right)

print(merge_sort([2,4,5,9,1,4]))