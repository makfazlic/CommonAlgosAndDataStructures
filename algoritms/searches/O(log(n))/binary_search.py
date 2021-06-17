# Binary search algorithm with log(n) complexity, precondition is that a list has to be sorted
# T(n) = O(log(n))

# A has to be a sorted list
def binary_search(A ,key):
    begin = 0
    end = len(A)
    while begin <= end:
        middle = (begin + end) // 2
        print(begin,end,middle)
        if begin == end:
            return False
        elif A[middle] == key:
            return True
        elif A[middle] > key:
            end = middle - 1
        else:
            begin = middle + 1
    return False

#print(binary_search([1,2,3,4,5,6,7,8,9,10],1))
#print(binary_search([1,2,3,4,5,6,7,8,9,10],5))
#print(binary_search([1,2,3,4,5,6,7,8,9,10],7))
#print(binary_search([1,2,3,4,5,6,7,8,9,10],9))
#print(binary_search([1,2,3,4,5,6,7,8,9,10],10))
#print(binary_search([1,2,3,4,5,6,7,8,9,10],0))