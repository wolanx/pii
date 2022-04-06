# 第三章

## 第1节： 1、二叉树（Binary-Tree）与经典问题

### 144. 二叉树的前序遍历

https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

```python
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []

        def dfs(node):
            if node:
                arr.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return arr
```

### 589. N 叉树的前序遍历

https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/

### 226. 翻转二叉树

https://leetcode-cn.com/problems/invert-binary-tree/

```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root or (not root.left and not root.right):
            return root
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root
```

### 102. 二叉树的层序遍历

https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        q = [root]
        ret = []

        while q:
            num = len(q)
            tmp = []
            for _ in range(num):
                cur = q.pop(0)
                tmp.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            ret.append(tmp)
        return ret
```

### 110. 平衡二叉树

https://leetcode-cn.com/problems/balanced-binary-tree/

```python
# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         self.leafIdx = None
#         self.flag = True
# 
#         def test(node, lv):
#             lv = lv + 1
#             if node:
#                 if not node.left or not node.right:
#                     if not self.leafIdx:
#                         self.leafIdx = lv  
#                     print(self.leafIdx, lv)
#                     if abs(self.leafIdx - lv) > 1:
#                         self.flag = False              
#                 test(node.left, lv)
#                 test(node.right, lv)
# 
#         test(root, 0)
#         return self.flag
```

### 112. 路径总和

https://leetcode-cn.com/problems/path-sum/
