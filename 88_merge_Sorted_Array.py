def merge(self, nums1, m, nums2, n):
        # taking lengts for both and then for inserting also at k position of nums1 list 
        i = m - 1
        j = n - 1
        k = m + n - 1
        # checking backward so given the array are in a sorted manner so taking element from nums 2 well check at nums of 1 n-1 length to check for sortedness and then finalising the answer of that we will insert the bigger one at k pos o
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1