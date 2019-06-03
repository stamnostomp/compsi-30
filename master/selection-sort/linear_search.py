def linear_search(mylist,item):
    for i in range (len(mylist)):
        if mylist[i]==item:
            return i
    return -1

mylist = [1,83,54,213,545]
print("number in list :", mylist)
x = int(input("enter a number to look fot :"))

result = linear_search(mylist,x)
if result==-1:
    print("number not in list")
else:
    print("number " + str(x) + "was found at position %d "%(result+1))
