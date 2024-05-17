class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        # Get the prefix store in res
        pre = 1
        for i, n in enumerate(nums):
            res.append(pre)
            pre *= n
        print (res)

        # calculate the postfix and at the same time finish the res
        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res