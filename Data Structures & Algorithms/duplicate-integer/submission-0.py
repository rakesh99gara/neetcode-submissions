class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set(nums)
        res = dict(zip(a, map(lambda x: nums.count(x), a)))
        return any(x > 1 for x in res.values())
        