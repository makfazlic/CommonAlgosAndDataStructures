# Searching algo with linear complexity
# T(n) = O(n)
import random

# Algorithms
def find_in_list(A, key):
    for item in A:
        if item == key:
            return True
    return False

# Unit tests
def test(number_of_tests):
    while number_of_tests > 0:
        array = []
        array_size = random.randint(0,50) # 100 maximum size 
        for item in range(array_size):
            array.append(random.randint(0,50))
        key = random.randint(0,50)
        print(find_in_list(array, key), key, array)
        number_of_tests = number_of_tests - 1
    return "Done"