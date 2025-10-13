nums=[1,1,1,5,7,8,9]
x=2
lb=-1
ub=len(nums)-1
while lb <=ub:
    mid=lb+(ub-lb)//2
    if nums[mid]>=x:
        lb=mid
        ub=mid-1
    else:
        lb=mid+1
# return lb