class Solution(object):
    def merge_sort(self, nums):
        result = []
        if len(nums) < 2:
            return nums
        mid = int(len(nums)/2)
        y = self.merge_sort(nums[:mid])
        z = self.merge_sort(nums[mid:])
        while (len(y) > 0) or (len(z) > 0):
            if len(y) > 0 and len(z) > 0:
                if y[0] > z[0]:
                    result.append(z[0])
                    z.pop(0)
                else:
                    result.append(y[0])
                    y.pop(0)
            elif len(z) > 0:
                for i in z:
                    result.append(i)
                    z.pop(0)
            else:
                for i in y:
                    result.append(i)
                    y.pop(0)
        return result
