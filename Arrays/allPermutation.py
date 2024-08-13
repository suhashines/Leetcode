nums = [1,2,3,4]

def allPermutation(nums,map,list=[]):

    if(len(list)==len(nums)):
        print(list)
        return

    for i in range(len(nums)):

        if(map[i]==0):

            list.append(nums[i])
            map[i] = 1

            allPermutation(nums,map,list)

            map[i]=0
            list.pop()

map = []

for i in range(len(nums)):
    map.append(0)

allPermutation(nums,map)