import random
nums = []
runtime=20

for x in range(runtime):
        tempnumis = [random.randint(1,20)]
        nums.append(tempnumis)

def insertionsort( nums ):
  for i in range( 1, len( nums ) ):
    tmp = nums[i]
    k = i
    while k > 0 and tmp < nums[k - 1]:
        nums[k] = nums[k - 1]
        k -= 1
    nums[k] = tmp

print ("Numbers", nums)
insertionsort(nums)
print ("Sorted numbers", nums)
