# Worst case complexity \Theta(n^2)
# But its normally \Theta(nlog(n))

# Function to do Partition
def partition(A, begin, end):
    i = begin          # checking index
    pivot = A[end]     # pivot
  
    for j in range(begin, end):
  
        # If current element is smaller than or
        # equal to pivot
        # Do the swap
        if A[j] <= pivot:
  
            # increment index of checking index
            i = i+1

            # swap q and i (from slides)
            A[i-1], A[j] = A[j], A[i-1]

    # Put the last element in between all beginings and ends then him
    A[i], A[end] = A[end], A[i]
    # return index of where partition is bla <= i <= bla
    return i

# Function to do Quicksort
def quickSort(A, begin, end):
    if len(A) == 1:
        return A
    if begin < end:
  
        # pi is partitioning index, A[p] is now
        # at right place
        pi = partition(A, begin, end)
  
        # Separately sort elements before
        # partition and after partition

        # This is the recursive call 1 Quicksort
        quickSort(A, begin, pi-1)

        # This is the recursive call 2 Quicksort
        quickSort(A, pi+1, end)
    return A
  
# Driver code to test above
A = [12, 4, 5, 16, 55, 2, 0]
print("Sorted Array is:")
print(quickSort(A, 0, len(A)-1))