# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
strs = ["flower","flow","flight"]
pf=""
for i in range(len(strs[0])):
    for s in strs:
        if i==len(s) or s[i]!=strs[0][i]:
            return pf