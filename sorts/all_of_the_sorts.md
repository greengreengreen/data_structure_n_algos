# All of the Sorts 
It is not very common to be asked about basic sorts in interviews. However, I think these basic sorting alogorithms help build intuitions. 

## Overview 
Sorting Algorithms | Average Time Complexity | Worst-case Time Complexity | Average Space Complexity | Worst-case Time Complexity 
Bubble Sort | O(n^2) | O(n^2) | O(1) | O(1) |
Selection Sort | O(n^2) | O(n^2) | O(1) | O(1) | 
Insertion Sort | O(n^2) | O(n^2) | O(1) | O(1) |
Quick Sort | O(n^2) | O(nlog(n)) | O(1) | O(1) | 
Heap Sort | O(nlog(n)) | O(nlog(n)) | O(1) | O(1) |
Merge Sort | O(nlog(n)) | O(nlog(n)) | O(n) | O(n) |

## Bubble Sort  
The reason why it is called bubble sort is that each time we only compare two adjacent elements. If arr[i] > arr[i+1], exchange arr[i] and arr[i+1]. Every time we compare two elements, we only carry the bigger element forward so that we carry the largest element at the end of the loop. Overall, we do (n-1) rounds of compares. At the kth round, we do the bubble exchange for arr[0:n-k+1] and make sure that the kth largest element is at arr[n-k]. 

```python 
def bubble_sort(arr):
    def exchange(cnt): 
        for i in range(1, cnt): 
            if arr[i] < arr[i-1]: 
                arr[i], arr[i-1] = arr[i-1], arr[i]
    n = len(arr)
    for i in range(n, 0, -1): 
        exchange(i)
    print(arr)
```

## Selection Sort  
Selection sort does n-1 loops. At loop i, it makes sure arr[:i+1] is sorted by traversing thru arr[i+1:] and compare them each with arr[i]. This makes arr[i] the i+1 th smallest element. 

``` python 
def selection_sort(arr): 
    n = len(arr)
    def exchange(start): 
        for i in range(start+1, n): 
            if  arr[i] < arr[start]: 
                arr[i], arr[start] = arr[start], arr[i] 
    for i in range(n-1): 
        exchange(i)
    print(arr)
```

## Insertion Sort  


```python 
def insertion_sort(arr): 
    def find_smaller(idx): 
        for i in range(idx-1, -1, -1): 
            if arr[i] < arr[i+1]: 
                break 
            else: 
                arr[i], arr[i+1] = arr[i+1], arr[i]
    n = len(arr)
    for i in range(1, n): 
        find_smaller(i)
    print(arr)
```

## Quick Sort 

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



## References: 
