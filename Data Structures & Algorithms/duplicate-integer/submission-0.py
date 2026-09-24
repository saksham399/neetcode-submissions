class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq = []
        for item in nums:
            if item not in uniq:
                uniq.append(item)
            else:
                return True
        return False