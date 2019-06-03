import random

runtime = 20
nums = []
def gnomesort(gns):
    i = 0
    while i < len(gns):
        if i == 0 or gns[i-1] <= gns[i]:
            i += 1
        else:
            gns[i], gns[i-1] = gns[i-1], gns[i]
            i -= 1

if __name__ == "__main__":
    for x in range(runtime):
        tempnumis = [random.randint(1,20)]
        nums.append(tempnumis)
    
    print ("Numbers", nums)
    gnomesort(nums)
    print ("Sorted numbers", nums)
