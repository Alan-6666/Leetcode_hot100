"""
分割 + merge
"""
#排序
def merge(left, right):
    i, j = 0, 0
    new_list = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            new_list.append(left[i])
            i += 1
        else:
            new_list.append(right[j])
            j += 1
            
    while i < len(left):
        new_list.append(left[i])
        i += 1
    while j < len(right):
        new_list.append(right[j])
        j += 1
        
    return new_list

def merge_sort(nums):
    if len(nums) <=1:
        return nums
    
    mid = len(nums) // 2
    
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)

nums = [5, 2, 3, 1]
nums = merge_sort(nums)

print(nums)