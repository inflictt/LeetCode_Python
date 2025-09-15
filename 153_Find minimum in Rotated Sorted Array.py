def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    mini = float("inf")
    n = len(nums)
    lo, hi = 0, n - 1
    while lo <= hi:
        mid = (lo + hi) // 2

        # right sorted or not
        if nums[mid] <= nums[hi]:
            mini = min(mini, nums[mid])
            hi = mid - 1

        # left sorted or not
        else:
            mini = min(mini, nums[lo])
            lo = mid + 1
    return mini
