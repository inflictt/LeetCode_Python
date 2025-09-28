def subsequence(index, subset, nums, result):
    if index == len(nums):
        result.append(subset.copy())
        return
    
    # Include the current element
    subset.append(nums[index])
    subsequence(index + 1, subset, nums, result)

    # Backtrack and exclude the current element
    subset.pop()
    subsequence(index + 1, subset, nums, result)


nums = [5, 9, 7]
result = []
subsequence(0, [], nums, result)
print(result)
