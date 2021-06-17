# Merge_R 
# Linear Complexity


# Need to fix
# Dont know if it belongs to this folder
def merge_r(A, B):
    if len(A)==0:
        return B
    if len(B)==0:
        return A

    if A[1] < B[1]:
        return [A[1]] + merge_r(A[:1], B)
    else:
        return [B[1]] + merge_r(A, B[:1])

print(merge_r([3,2,1],[5,6,2]))