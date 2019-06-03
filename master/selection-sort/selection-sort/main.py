import random
userint = int(input("input how long you would like your list"))
my_list = []
my_list = random.sample(range(1,101),userint)
def selectionSort(alist):
   for i in range(len(alist)):

      # find min vaule
       minPosition = i

       for j in range(i+1, len(alist)):
           if alist[minPosition] > alist[j]:
               minPosition = j

       # swap with the first
       temp = alist[i]
       alist[i] = alist[minPosition]
       alist[minPosition] = temp

   return alist
print(selectionSort(my_list))
