nums = [1,1,1,2,2,3]
arr = []
count = 0
first, second = 0, 1

for i in range(len(nums) - 1):
    if nums[first] == nums[second]:
        arr.append(nums[first])
        count += 1
        if count > 2:
            arr.remove(arr[first])        
    elif nums[first] != nums[second]:
        count = 0
    first += 1
    second += 1

    
print(arr)