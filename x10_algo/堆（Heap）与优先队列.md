# 第三章

## 第2节 2、堆（Heap）与优先队列

> 找 top N 问题

### 剑指 Offer 40. 最小的k个数

https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/

```text
最小堆 O(n) 弹出 k 次
最大堆 O(k) 始终维护 k 个数
```

### 1046. 最后一块石头的重量

https://leetcode-cn.com/problems/last-stone-weight/

```
最大堆
x = h.pop()
y = h.pop()
if (x != y) {
    h.push(y - x)
}
```

### 215. 数组中的第K个最大元素

https://leetcode-cn.com/problems/kth-largest-element-in-an-array/

```text
最小堆 找最大的数
```

### 703. 数据流中的第 K 大元素

https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/

```text
业务 class 版本的
```

### 692. 前K个高频单词

https://leetcode-cn.com/problems/top-k-frequent-words/

```text
先给没个词算个次数
再 大顶堆
再 字典序
```

### 295. 数据流的中位数

困难 https://leetcode-cn.com/problems/find-median-from-data-stream/

```text
small heap
large heap
```

### 264. 丑数 II

https://leetcode-cn.com/problems/ugly-number-ii/

```text
for n
    if set ! exist *2 *3 *5
        h.push()
        set.put()
return h.top()
```

### 373. 查找和最小的 K 对数字

https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums/

```text
# 时间超出
for
    for
        h.push(a + b)
        if h.size > k
            h.pop()

# 多路归并，取单区一个
{1,2,3}
{2,3,4}
{3,4,5}
```
