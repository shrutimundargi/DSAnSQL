#Given an integer array, nums, find and return all unique triplets [nums[i], nums[j], nums[k]], such that i ≠= j, i ≠= k, and j ≠= k and nums[i] + nums[j] + nums[k] ==0==0.


def three_sum(nums):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        if nums[i] > 0:
            break
        
        if i == 0 or nums[i] != nums[i - 1]:
            low, high = i + 1, n - 1
            
            while low < high:
                sum = nums[i] + nums[low] + nums[high]
                
                if sum < 0:
                    low += 1
                elif sum > 0:
                    high -= 1
                else:
                    result.append([nums[i], nums[low], nums[high]])
                    
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
    
    return result


