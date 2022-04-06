# 第三章

## 第3节： 3、并查集（Union-find）及经典问题

> 找祖先

```python
from typing import List


class UnionFind:
    def find(self):
        ...

    def merge(self):
        ...
```

- Quick-Find

- Quick-Union 树

```text
def __init__(size):
    for i in range(size):
        father[i] = i
def find(x):
    int root = x;
    while (root != father[root]) {
        root = father[root]
    }
    return root;
def merge(x, y):
    rootX = find(x)
    rootY = find(y)
    if (rootX == rootY) return
    father[rootX] = rootY
```

- Weighted Quick-Union 优化 树高问题，矮的=》高的，小的=》大的

```text
def __init__(size):
    for i in range(size):
        father[i] = i
def find(x):
    int root = x;
    while (root != father[root]) {
        root = father[root]
    }
    return root;
def merge(x, y):
    rootX = find(x)
    rootY = find(y)
    if (rootX == rootY) return
    father[rootX] = rootY
```

- Weighted Quick-Union with path compression 路径压缩

```text

```

### 547. 省份数量

https://leetcode-cn.com/problems/number-of-provinces/

### 200. 岛屿数量

https://leetcode-cn.com/problems/number-of-islands/

```text
i * m + j
➡️ ⬇️ 只需要
```

### 990. 等式方程的可满足性

https://leetcode-cn.com/problems/satisfiability-of-equality-equations/

```python
class Solution:
    def equationsPossible(self, arr: List[str]) -> bool:
        uf = UnionFind(26)
        for i in arr:
            x = arr[0]
            y = arr[3]
            if arr[1] == '=':  # 先做 连接的
                uf.merge(x, y)
        for i in arr:
            x = arr[0]
            y = arr[3]
            if arr[1] == '!' and uf.find(x) == uf.find(y):  # 坚持 不连接 的满足不
                return False
        return True
```

### 1319. 连通网络的操作次数

https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected/

```text
网线优化问题，用最少的线
merge次数 - 集合元素 + 1
```

### 684. 冗余连接

https://leetcode-cn.com/problems/redundant-connection/

```text
if uf.find(x) == uf.find(y):
    ans = edge[i]
    break
```

### 947. 移除最多的同行或同列石头

https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column/

```python
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if 0 == 0 or 1 == 1:
                    uf.merge(i, j)
        cnt = 0
        for i in range(n):
            if uf.find(i) == i:
                cnt += 1
        return n - cnt
```

### 1202. 交换字符串中的元素

https://leetcode-cn.com/problems/smallest-string-with-swaps/

### 765. 情侣牵手

https://leetcode-cn.com/problems/couples-holding-hands/

```text
n 2n
node = pair{0,1}
{0, 2} => {0/2, 2/2} =>  {0, 1}
```
