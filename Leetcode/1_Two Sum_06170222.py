class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            n=target-i
            if n in nums: 
                if i != n:
                    return [nums.index(i),nums.index(n)]
                elif i == n and nums.count(i)>=2:
                    a=nums.index(i)
                    nums.remove(i)
                    b=nums.index(n)+1
                    return [a,b]
