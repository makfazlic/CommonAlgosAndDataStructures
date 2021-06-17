# Merge of two arrays A and B
# Complexity Linear

def merge(A, B):
    i = 0
    j = 0
    X = []
    while i < len(A) or j < len(B):
        if i < len(A) and (j >= len(B) or A[i] < B[j]):
            X.append(A[i])
            print("i",X)
            i += 1
        else:
            X.append(B[j])
            print("j",X)
            j += 1
    return X

print(merge([5,7,1,3,4,5,2],[2,4,5,9,1,4]))