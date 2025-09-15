nums = [10, 11, 11, 12, 12, 13, 13, 13, 1, 2, 3, 4]
n = len(nums)
target = 11
lo, hi = 0, n - 1


def search(nums, n, target, lo, hi):
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
                return True
        #here to eliminate the duplicate we did this for lo and hi as to remove them
        if nums[lo]==nums[mid]==nums[hi]:
            lo+=1
            hi-=1
            continue
        #checking for the position of the target
        if nums[mid] <= nums[hi]:
            if(nums[mid]<=target<=nums[hi]):
                lo=mid+1
            else:    
                hi=mid-1 
        else:
            if(nums[lo]<=target<=nums[mid]):
                hi=mid-1
            else:
                lo=mid+1
    return False
check=search(nums, n, target, lo, hi)
print("ans is ", check)