class Solution:

    def isSameTree(self, p, q):
        stack = [(p, q)]
        while stack:
            (p, q) = stack.pop()
            if p and q and p.val == q.val:
                stack.extend([
                    (p.left,  q.left),
                    (p.right, q.right)
                ])
            elif p or q:
                return False
        return True
