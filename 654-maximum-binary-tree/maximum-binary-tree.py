class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None

        max_val = max(nums)
        mid = nums.index(max_val)

        root = TreeNode(max_val)

        root.left = self.constructMaximumBinaryTree(nums[:mid])
        root.right = self.constructMaximumBinaryTree(nums[mid + 1:])

        return root
