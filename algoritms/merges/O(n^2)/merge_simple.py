# Merging algo with exponential complexity
# T(n) = O(n^2)

def merge_simple(A,B): # A and B are arrays
    merged = []

    for i in range(len(A)):
        if not find_in_list(merged,A[i]):
            merged.append(A[i])

    for i in range(len(B)):
        if not find_in_list(merged,B[i]) and not find_in_list(merged,B[i]):
            merged.append(B[i])
    return merged


#print(merge_simple([1,2,3,4],[5,6,7,4,8]))
#print(merge_simple([1,5,8,12,4,5,6,14,4],[5,6,7,4,4,6,1,8]))
#print(merge_simple([2,2,2,2,2],[2,2,2,2,2]))
#print(merge_simple([1,2,3,4],[1,2,3,4]))
#print(merge_simple([-1,-2,-3,-4],[-1,-2,-3,-4]))