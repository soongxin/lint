class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_hash = {}
        rtype = []
        for i in range(0, len(nums)):
            nums_hash[nums[i]] = i

        keys = nums_hash.keys()
        for j in range(0, int(target/2)+1):
            sub = target - j
            if j in keys and sub in keys:
                rtype = [nums_hash[j], nums_hash[sub]]

        return rtype



s = Solution()
print(s.twoSum([3, 4], 7))


