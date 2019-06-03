from math import floor

def binary_search(array, search_term):
    n = len(array)
    L = 0
    R = n-1

    while L <= R:
        mid = floor((L+R)/2)
        if array[mid] < search_term:
            L = mid + 1
        elif array[mid] > search_term:
            R = mid -1

        else:
            return mid
    return -1

A = [1,2,3,4,5,6,7,8,9,10]
print(A)
term = int(input("wthat number are you looking for :"))
index = binary_search(A, term)
if index >= 0:
    print("{} is at index {}".format(A[index], index))

else:
    print("could not find the term")

