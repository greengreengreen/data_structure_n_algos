# All of the Sorts 
It is not very common to be asked about basic sorts in interviews. However, I think these basic sorting alogorithms help build intuitions. 

## Overview 
Sorting Algorithms | Average Time Complexity | Worst-case Time Complexity | Average Space Complexity | Worst-case Time Complexity 
---- | --- | ---- | --- | --- |
Bubble Sort | O(n^2) | O(n^2) | O(1) | O(1) |
Selection Sort | O(n^2) | O(n^2) | O(1) | O(1) | 
Insertion Sort | O(n^2) | O(n^2) | O(1) | O(1) |
Quick Sort | O(nlog(n)) | O(n^2)  | O(1) | O(1) | 
Heap Sort | O(nlog(n)) | O(nlog(n)) | O(1) | O(1) |
Merge Sort | O(nlog(n)) | O(nlog(n)) | O(n) | O(n) |

## Bubble Sort  
The reason why it is called bubble sort is that each time we only compare two adjacent elements. If arr[j] < arr[j-1], exchange arr[j] and arr[j-1]. Every time we compare two elements, we only carry the bigger element forward so that we carry the largest element at the end of the loop. Overall, we do n rounds of compares. At the i th round, we do the bubble exchange for arr[0:i] and make sure that the i th largest element is at arr[n-i]. 

```python 
def bubble_sort(arr):
    def exchange(cnt): 
        for j in range(1, cnt): 
            if arr[j] < arr[j-1]: 
                arr[j], arr[j-1] = arr[j-1], arr[j]
    n = len(arr)
    for i in range(n, 0, -1): 
        exchange(i)
```

## Selection Sort  
Selection sort does n-1 loops. At loop i, it makes sure arr[:i+1] is sorted by traversing thru arr[i+1:] and compare them each with arr[i]. This makes arr[i] the i+1 th smallest element in arr[i+1:]. </br>

Notice that in exchange function, bubble sort does not always exchange adjacent elements. It focuses on making arr[start] the smallest element in arr[start:]. 

``` python 
def selection_sort(arr): 
    n = len(arr)
    def exchange(start): 
        for j in range(start+1, n): 
            if  arr[j] < arr[start]: 
                arr[j], arr[start] = arr[start], arr[j] 
    for i in range(n-1): 
        exchange(i)
```

## Insertion Sort  
In each loop i, both selection sort and insertion sort maintains arr[:i+1] to be sorted, yet in a different way than how selection sort does. In order to keep arr[:i+1] sorted, it will move arr[i] to the right position in arr[:i+1]. The right position is when arr[i] encounters the first smaller element. 

```python 
def insertion_sort(arr): 
    def find_smaller(idx): 
        for j in range(idx-1, -1, -1): 
            if arr[j] < arr[j+1]: 
                break 
            else: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    n = len(arr)
    for i in range(1, n): 
        find_smaller(i)
```

## Quick Sort 
I have shown two ways to do quick sort here, including recursive and interative. So the basic idea of quick sort is partition. 1. We randomly pick an splitting index idx. 
2. Move all the elements smaller than arr[idx] to the left and all the larger elements to the right.
3. Find the adjusted position for arr[idx] => idx_new. 
4. Keep doing 1~3 until each element is sorted. 

```python 
def quick_sort_rcur(arr): 
    def sort(idx, l, r):
        arr[r], arr[idx] = arr[idx], arr[r] 
        less_than_idx = l 
        for i in range(l, r): 
            if arr[i] < arr[r]: 
                arr[i], arr[less_than_idx] = arr[less_than_idx], arr[i]
                less_than_idx += 1
        arr[less_than_idx], arr[r] = arr[r], arr[less_than_idx]
        return less_than_idx

    def partition(l, r): 
        if l >= r: return 
        idx = random.randint(l, r)
        idx_new = sort(idx, l, r)
        partition(l, idx_new-1)
        partition(idx_new+1, r)
    
    partition(0, len(arr)-1)
``` 

For iterative method, use a stack to store the newly split range. 
Q: Why stack not queue? 
A: Actually, either queue or stack should work. There no dependency or priority between these ranges.

```python 
def quick_sort_iter(arr): 

    def sort(idx, l, r):
        arr[r], arr[idx] = arr[idx], arr[r]
        less_than_idx = l
        for i in range(l, r):
            if arr[i] < arr[r]:
                arr[i], arr[less_than_idx] = arr[less_than_idx], arr[i]
                less_than_idx += 1
        arr[less_than_idx], arr[r] = arr[r], arr[less_than_idx]
        return less_than_idx

    n = len(arr)
    stack = [(0, n-1)]
    while stack: 
        l, r = stack.pop() 
        if l >= r: continue 
        idx = random.randint(l, r)
        idx_new = sort(idx, l, r)
        stack.append((l, idx_new-1))
        stack.append((idx_new+1, r))
```

## Heap Sort 
The basic idea of heap sort is to think of an array as a binary tree. For each parent node in this binary tree, it has a value which is greater than its left child and right child. Therefore, the root of this tree is the largest element in the array. This is called a max heap. 
heapify function takes O(log(n)) time. What does it do? After we removing the max item which is the root, from the tree, we put its last element in the array in the root position temporarily. So we need to make sure this new tree is legitimate. We check the new root node and compare it with its children until it finds its right position. 

Q: Why do we put the last element in the array as the new temp root? 
A: Think about a tree with no root node and need to get one of the other node into the root position. If we move any node other than the last node, then based on the array-tree illustration, there will be a big change in the tree and you would expect more than one node become ilegal. However, if we move the last node to the root, then only the new root node is ilegal. Just applying heapify function to the new root solves the problem. 


```python 
def heap_sort(arr): 
    def heapify(l, r):
        cur = l 
        while cur < r: 
            left_child = 2 * cur + 1
            right_child = 2 * cur + 2 
            biggest_idx = cur
            if left_child < r and arr[left_child] > arr[biggest_idx]: biggest_idx = left_child 
            if right_child < r and arr[right_child] > arr[biggest_idx]: biggest_idx = right_child
            if biggest_idx == cur: 
                break 
            else:
                arr[biggest_idx], arr[cur] = arr[cur], arr[biggest_idx] 
                cur = biggest_idx 
    n = len(arr)
    for i in range(n//2, -1, -1): 
        heapify(i, n)
    for i in range(n-1): 
        arr[0], arr[n-i-1] = arr[n-i-1], arr[0]
        heapify(0, n-i-1)
```

## Merge Sort 
Merge sort is different from all the other sorts in that it needs extra O(n) space inevitably. The basic idea of merge sort is divide and conquer. We partition one array into two array and sorted the two. Then we pick one element from the two sorted array and put the smaller one into the new array. In this way, when we are done comparing the two sorted array, the new array will be sorted and contain all the elements.  

```python 
def merge_sort_rcur(arr): 
    n = len(arr)
    if n <= 1: return arr 
    left, right = merge_sort_rcur(arr[:n//2]), merge_sort_rcur(arr[n//2:])
    res = []
    while left and right: 
        if left[0] < right[0]: res.append(left.pop(0))
        else: res.append(right.pop(0))
    if left: res += left 
    if right: res += right 
    return res 
```

```python
def merge_sort_iter(arr):  
    def merge(start, delta): 
        left = arr[start: start+delta]
        right = arr[start+delta: start+2*delta]
        res = []
        while left and right: 
            if left[0] < right[0]: res.append(left.pop(0))
            else: res.append(right.pop(0))
        if left: res += left 
        if right: res += right 
        return res 

    n = len(arr)
    sub_len = 1
    while sub_len < n: 
        for i in range(0, n, 2*sub_len): 
            arr[i: i+2*sub_len] = merge(i, sub_len)
        sub_len *= 2 
    return arr   
```


## Conclusion: 
Basic sorting algorithms are must knows. Some problems to practice are as follows: 
1. [LC 215 Kth Largest Element in An Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
2. [LC 912 Sort An Array](https://leetcode.com/problems/sort-an-array/)

## References: 
[The most straightforward tutorial about bubble sort, insertion sort and selection sort.](https://www.youtube.com/channel/UCIqiLefbVHsOAXDAxQJH7Xw)
