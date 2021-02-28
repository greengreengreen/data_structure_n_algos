Binary Search Basics

This article is for my future self or anyone like me who would want a clear explanation on different form of binary search. 

## Basic form: 
Given a sorted array, find the index which has value = target. 

## Possible exceptional scenarios: 
1. This value may not exist in the array. 
2. There could be more than one value exists in the array, which one to return? 

## Why is binary search powerful?
The reason why binary search is so powerful is that the criteria does not have to be value == target. It could be any criteria, be it value > target, value < target and etc. Be imaginative:)

## Things to consider before writing a binary search: 
1. What is the criteria? The criteria is a function that returns true/false. 
2. Is the monotone style inscrease or descrease? 
    * Increase: if criteria is valid at index i, then the criteria is valid on any index j such that j > i; 
    * Decrease: if criteria is valid at index i, then the criteria is valid on any index j such that j < i; 
3. Which index to return? the first index or the last index which qualifies the criteria? 

Based on the above considerations, I listed below variants of binary search. In this article, I will show how each of the variant is implemented.

variant |   criteria  |  monotone:inc/desc |   index:first/last|
------- | ----------- | ------------------ | ----------------- |
1       | value == target | inc     | first |
2       | value == target | desc    | first |
3       | value == target | inc     | last |
4       | value == target | desc    | last|
5       | value > target  | inc     | first|
6       | value >= target | inc     | first  |
7       | value > target  | desc    | last|
8       | value >= target | desc    | last|
9       | value < target  | inc     | last|
10      | value <= target | inc     | last|
11      | value < target  | desc    | first|
12      | value <= target | desc    | first|

1. Given an increasingly sorted array, return the first index which has value == target.  
```python 
def binary_search_var1(arr, target): 
    # 1. Given an increasingly sorted array, return the first index which has value == target.
    n = len(arr)
    l, r = 0, n 
    while l < r: 
        m = l + (r-l)//2 
        if arr[m] >= target: r = m
        else: l = m + 1
    return l if l < n and arr[l] == target else -1 
```

2. Given a descreasingly sorted array, return the first index which has value == target.  

```python 
def binary_search_var2(arr, target):
    # 2. Given a descreasingly sorted array, return the first index which has value == target.
    n = len(arr)
    l, r = 0, n 
    while l < r: 
        m = l + (r-l)//2 
        if arr[m] <= target: r = m 
        else: l = m + 1
    return l if l < n and arr[l] == target else -1 
```

3. Given a increasingly sorted array, return the last index which has value == target.

```python 
def binary_search_var3(arr, target):
    # 3. Given a increasingly sorted array, return the last index which has value == target.
    n = len(arr)
    l, r = -1, n-1 
    while l < r: 
        m = l + math.ceil((r-l)/2)
        if arr[m] <= target: l = m 
        else: r = m - 1
    return r if r >= 0 and arr[r] == target else -1 
```

4. Given a descreasingly sorted array, return the last index which has value == target.

```python 
def binary_search_var4(arr, target):
    # 4. Given a descreasingly sorted array, return the last index which has value == target.
    n = len(arr)
    l, r = -1, n-1 
    while l < r: 
        m = l + math.ceil((r-l)/2)
        if arr[m] >= target: l = m 
        else: r = m-1 
    return r if r >= 0 and arr[r] == target else -1 
```


5. Given a increasingly sorted array, return the first index which has value > target.

```python 
def binary_search_var5(arr, target):
    # 5. Given a increasingly sorted array, return the first index which has value > target.
    n = len(arr)
    l, r = 0, n 
    while l < r:
        m = l + (r-l)//2 
        if arr[m] > target: r = m 
        else: l = m + 1
    return l if l < n and arr[l] > target else -1 

```


6. Given a increasingly sorted array, return the first index which has value >= target.

```python 
def binary_search_var6(arr, target):
    # 6. Given a increasingly sorted array, return the first index which has value >= target.
    n = len(arr)
    l, r = 0, n 
    while l < r: 
        m = l + (r-l)//2 
        if arr[m] >= target: r = m 
        else: l = m + 1
    return l if l >= 0 and arr[l] >= target else -1 

```



7. Given a descreasingly sorted array, return the last index which has value > target.

```python 
def binary_search_var7(arr, target): 
    # 7. Given a descreasingly sorted array, return the last index which has value > target.
    n = len(arr)
    l, r = -1, n-1
    while l < r: 
        m = l + math.ceil((r-l)/2)
        if arr[m] > target: l = m 
        else: r = m - 1
    return r if r >= 0 and arr[r] > target else -1 
```

8. Given a descreasingly sorted array, return the last index which has value >= target.

```python 
def binary_search_var8(arr, target):
    # 8. Given a descreasingly sorted array, return the last index which has value >= target.
    n = len(arr)
    l, r = -1, n-1 
    while l < r: 
        m = l + math.ceil((r-l)/2)
        if arr[m] >= target: l = m 
        else: r = m -1 
    return r if r >= 0 and arr[r] >= target else -1 
```


9. Given a increasingly sorted array, return the last index which has value < target.

```python 
def binary_search_var9(arr, target): 
    # 9. Given a increasingly sorted array, return the last index which has value < target.
    n = len(arr)
    l, r = -1, n-1 
    while l < r: 
        m = l + math.ceil((r-l)/2)
        if arr[m] < target: l = m 
        else: r = m - 1
    return r if r >= 0 and arr[m] < target else -1

```


10. Given a increasingly sorted array, return the last index which has value <= target.
```python 
def binary_search_var10(arr, target): 
    # 10. Given a increasingly sorted array, return the last index which has value <= target.
    n = len(arr)
    l, r = -1, n-1 
    while l < r: 
        m = l + math.ceil((r-l)/2)
        if arr[m] <= target: l = m 
        else: r = m - 1
    return r if r >= 0 and arr[r] <= target else -1

```

11. Given a descreasingly sorted array, return the first index which has value < target.

```python 
def binary_search_var11(arr, target): 
    # 11. Given a descreasingly sorted array, return the first index which has value < target.
    n = len(arr) 
    l, r = 0, n
    while l < r: 
        m = l + (r-l)//2 
        if arr[m] < target: r = m 
        else: l = m + 1
    return l if l < n and arr[l] < target else -1 
```

12. Given a descreasingly sorted array, return the first index which has value <= target.

```python 
def binary_search_var12(arr, target): 
    # 12. Given a descreasingly sorted array, return the first index which has value <= target.
    n = len(arr)
    l, r = 0, n 
    while l < r: 
        m = l + (r-l)//2 
        if arr[m] <= target: r = m 
        else: l = m + 1
    return l if l < n and arr[l] <= target else -1 
```

## Patterns observed
### P1: first or last qualified index? 
Since indexes are integers, when we try to find the middle index m, we usually have two options: ceiling or floor. 
####  What is ceiling and floor? 
Ceiling means: m = l + math.ceil((r-l)/2). floor means: m = l + (r-l)//2 . Imagine if the array only have two elements and currently l = 0, r = 1, then ceiling will always return m = 1 and floor will always return m = 0. 
#### Why does ceiling/floor matter? 
Provided that we are trying to catch the first qualified index, 
if we use ceiling, then whenever r-l is odd, m will be (r-l)/2 + 0.5. For example, when l = 0, r = 1, ceiling will always return m = 1. In this case, we will never be able to test whether or not arr[0] qualifies. And arr[0] could be the first qualified index. Therefore, if we use ceiling method to get the first qualified index, we might never be able to catch and fall into infinite loop. 
#### How to use ceiling/floor? 
So far, we know that when getting the first qualified index, we use floor. For last qualified index, we use ceiling. However, floor/ceiling does not come alone. It must be paired with the correct starting indexes. For example, we are getting the last qualified index and we use ceiling. Say, len(arr) = n and starting index l = 0, r = n-1. Note that, in this case we will never be able to test arr[0] because of the ceiling method. When we approach l = 0, r = 1, all we can get is m = 1 and we are stuck. </br>
That said, 
when getting the first qualified index, we use starting index: l = 0, r = n along with floor method. 
when getting the last qualified index, we use starting index: l = -1, r = n-1 along with ceiling method. 

### P2: when to use l = m, l = m+1, r = m, r = m-1? 
This is a question of when l == r and break the while condition. 
Regarding to the last loop before while condition was broken, what happened? 
For the pair (l = m , r = m-1), 
Obviously we are looking for the last qualified index and m = l + math.ceil((r-l)/2).
When it is an increasing monotone, which means, 
if arr[i] statisfis the criteria, any j such that j > i qualifies. 
a. if the last loop makes l = m, then the last r = m. The second last l = m-1.
b. if the last loop makes r = m-1, then the last l = m-1. The second last r = m+1 or m.  
Similar analysis goes when there is descreasing monotone and when we need to find the first qualified index. 
Conclusion: The while condition can be broke from either side, left or right. 









