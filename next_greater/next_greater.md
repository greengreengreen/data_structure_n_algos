# Next Greater Problem And Its Homies

> You got a new friend. well. I got homies. — Heartless by Kanye West

It is very common to see the next greater element problems these days. In this article, I will go from solving the vanilla form of this problem to analyzing and illustrating some of its the variants. I will talk about when to sort, how to traverse (from left or right) and when we will need an auxiliary array. 

## Overview
* [Vanilla form](#vanilla-form): Given an array A, for each element at index i, find eligible indexes j such that A[i] < A[j] and i < j. 
* [Variant1](#variant1): Vanilla form + for all the eligible js of index i, find the j such that A[j] the smallest one
* [Variant2](#variant2): Vanilla form + for all the eligible js of index i, find the j such that A[j] the smallest one.
* [Variant3](#variant3): Vanilla form + for all the eligible js of index i, find the j such that j is the largest.
* [Variant4](#variant4): Vanilla form + for all the eligible js of index i, find the j such that j is the smallest.
* [Variant5](#variant5): Vanilla form + for all the eligible js of index i, find the largest j such that any element between [i+1, j] is larger than A[i].

## Vanilla form
### Problem Statement
Given an array A, for each element at index i, find eligible indexes j such that A[i] < A[j] and i < j. 
### Examples 
Example1: 
```
A  =  [1,  6,  2,  7,  8,  0]</br>
then    at index 0, A[0] = 1. eligible js are: 1, 2, 3, 4. because A[1] > A[0], A[2] > A[0], A[3] > A[0], A[4] > A[0]. 
                                                        Since A[5] < A[0], index 5 does not qualify. 
        at index 1, A[1] = 6, eligible js are: 3, 4 
        at index 2, A[2] = 2, eligible js are: 3, 4
        at index 3, A[3] = 7, eligible js are: 4 
        at index 4, A[4] = 8, No eligible j 
        at index 5, A[5] = 0, No eligible j 
Hence, res = [[1, 2, 3, 4], [3, 4], [4], [], []]
```

Example2: 
```
A = [5, 0, 2, 1, 3, 4]  => res = [[], [2, 3, 4, 5], [4, 5], [4, 5], [5], []]
```

### Brute Force
An obvious way is brutal force, for each element i, loop from i+1 to the end of the array, add all the js which satisfies A[j] > A[i]. 
Time Complexity: O(n^2)
```python
def baseForm(A): 
    n = len(A)
    res = [[] for i in range(n)] 
    for i in range(n): 
        for j in range(i+1, n): 
            if A[j] > A[i]: 
                res[i].append(j) 
    return res 
``` 
Can we do better than O(n^2)? 
Yes. We can make it O(nlogn). Of course O(nlogn) didn’t count the time to copy indexes into the result array. 
There are several ways to achieve this. 
    1. Binary Search 
    2. Merge Sort 
    3. Binary Index Tree 
Since the base form optimization is not the focus of this post, I will create another post for it. 

## Variant1
> Vanilla form + for all the eligible js of index i, find the j such that A[j] the largest one.

### Problem statement: 
Given an array A, for each element at index i, among all the eligible indexes j such that A[i] < A[j] and i < j, find the j such that A[j] is the largest one. 

### Examples: 
Example1: 
```
A       =  [1,  6,  2,  7,  8,  0]
then at index 0, A[0] = 1, among eligible js including: 1, 2, 3, 4.  A[4] > A[3] > A[1] > A[2]
        at index 1, A[1] = 6, among eligible js including: 3, 4, A[4] > A[3]
        at index 2, A[2] = 2, among eligible js including: 3, 4, A[4] > A[3]
        at index 3, A[3] = 7, only one eligible j: 4 
        at index 4, A[4] = 8, No eligible j 
        at index 5, A[5] = 0, No eligible j 
Hence, res = [4, 4, 4, 4, -1, -1]
```
Example2: 
```
A = [5, 0, 2, 1, 3, 4]  => res = [-1, 5, 5, 5, 5, -1]
```

### Brute Force: O(n^2)
``` python
def v1_brute_force(A): 
    n = len(A)
    res = [-1] * n 
    for i in range(n): 
        for j in range(i+1, n): 
            if A[j] > A[i]:
                if res[i] == -1 or A[res[i]] < A[j]: 
                    res[i] = j 
    return res
``` 

### With technique: O(n)
``` python
def v1_adv(A):
    n = len(A)
    res = [-1] * n
    maxidx = n-1
    for i in range(n-2, -1, -1):
        if A[maxidx] > A[i]:
            res[i] = maxidx
        else:
            maxidx = i
    return res
```

## Variant2
>Vanilla form + for all the eligible js of index i, find the j such that A[j] the smallest one.
### Problem statement 
Given an array A, for each element at index i, among all the eligible indexes j such that A[i] < A[j] and i < j, find the j such that A[j] is the smallest one. 
### Examples

Example1: 
```
A       =  [1,  6,  2,  7,  8,  0]
then at index 0, A[0] = 1, among eligible js including: 1, 2, 3, 4.  A[4] > A[3] > A[1] > A[2]
        at index 1, A[1] = 6, among eligible js including: 3, 4, A[4] > A[3]
        at index 2, A[2] = 2, among eligible js including: 3, 4, A[4] > A[3]
        at index 3, A[3] = 7, only one eligible j: 4 
        at index 4, A[4] = 8, No eligible j 
        at index 5, A[5] = 0, No eligible j 
Hence, res = [2, 3, 3, 4, -1, -1]
```
Example2: 
```
A = [5, 0, 2, 1, 3, 4]  => res = [-1, 3, 4, 4, 5, -1]
```

### Brute Force: O(n^2)
```python
def v2_brute_force(A):
    n = len(A)
    res = [-1] * n
    for i in range(n):
        for j in range(i, n):
            if A[j] > A[i]:
                if res[i] == -1 or A[res[i]] > A[j]:
                    res[i] = j
    return res
```
### With technique: O(nlogn)
```python 
def v2_adv(A):
    arr = sorted([(num, i) for i, num in enumerate(A)])
    n = len(A)
    res = [-1] * n
    stack = []
    for num, i in arr:
        while stack and stack[-1] < i:
            res[stack.pop()] = i
        stack.append(i)
    return res
```

## Variant3
>Vanilla form + for all the eligible js of index i, find the j such that j is the largest.

### Problem statement: 
Given an array A, for each element at index i, among all the eligible indexes j such that A[i] < A[j] and i < j, find the j such that j is the largest. 

### Examples
Example1: 
```
A       =  [1,  6,  2,  8,  7,  0]
then at index 0, A[0] = 1, eligible js including: 1, 2, 3, 4.  
        at index 1, A[1] = 6, eligible js including: 3, 4
        at index 2, A[2] = 2, eligible js including: 3, 4
        at index 3, A[3] = 8, No eligible j 
        at index 4, A[4] = 7, No eligible j 
        at index 5, A[5] = 0, No eligible j 
Hence, res = [4, 4, 4, -1, -1, -1]
```
Example2: 
```
A = [5, 4, 1, 3, 2, 0]  => res = [-1, -1, 4, -1, -1, -1]
```
### Brute Force: O(n^2)
```python
def v3_brute_force(A): 
    n = len(A)
    res = [-1] * n 
    for i in range(n): 
        for j in range(n-1, i, -1): 
            if A[j] > A[i]: 
                res[i] = j 
                break 
    return res 
```
### With technique:  O(nlogn)
```python
def v3_adv(A): 
    n = len(A)
    res = [-1] * n 
    q = []
    for i in range(n-1, -1, -1): 
        l, r = 0, len(q)
        while l < r: 
            m = l + (r-l)//2
            if A[q[m]] <= A[i]: l = m + 1
            else: r = m
        if l < len(q): res[i] = q[l]
        if (not q) or (A[q[-1]] < A[i]): 
            q.append(i)
    return res
```
## Variant4
>Vanilla form + for all the eligible js of index i, find the j such that j is the smallest.
### Problem statement: 
Given an array A, for each element at index i, among all the eligible indexes j such that A[i] < A[j] and i < j, find the j such that A[j] is the smallest one. 
### Examples: 
Example1: 
```
A       =  [1,  6,  2,  8,  7,  0]
index:     0   1   2   3   4   5
then at index 0, A[0] = 1, eligible js including: 1, 2, 3, 4.  
        at index 1, A[1] = 6, eligible js including: 3, 4
        at index 2, A[2] = 2, eligible js including: 3, 4
        at index 3, A[3] = 8, No eligible j 
        at index 4, A[4] = 7, No eligible j 
        at index 5, A[5] = 0, No eligible j 
Hence, res = [1, 3, 3, -1, -1, -1]
```
Example2: 
```
A = [5, 4, 1, 3, 2, 0]  => res = [-1, -1, 3, -1, -1, -1]
```

### Brute Force: 
```python
def v4_brute_force(A): 
    n = len(A)
    res = [-1] * n 
    for i in range(n): 
        for j in range(i+1, n): 
            if A[j] > A[i]: 
                res[i] = j 
                break 
    return res 
```
### With technique: 
```python
def v4_adv(A): 
    n = len(A)
    res = [-1] * n
    stack = []
    for i in range(n): 
        while stack and A[stack[-1]] < A[i]: 
            res[stack.pop()] = i 
        stack.append(i)
    return res
```

## Variant5
>Vanilla form + for all the eligible js of index i, find the largest j such that any element between [i+1, j] is larger than A[i].
### Problem statement: 
Given an array A, for each element at index i, among all the eligible indexes j such that A[i] < A[j] and i < j, find the largest j such that any element between [i+1, j] is larger than A[i]
### Examples
Example1: 
```
A       =  [1,  6,  2,  8,  7,  0]
then at index 0, A[0] = 1, eligible js including: 1, 2, 3, 4.  
        at index 1, A[1] = 6, eligible js including: 3, 4
        at index 2, A[2] = 2, eligible js including: 3, 4
        at index 3, A[3] = 8, No eligible j 
        at index 4, A[4] = 7, No eligible j 
        at index 5, A[5] = 0, No eligible j 
Hence, res = [4, -1, 4, -1, -1, -1]
```
Example2: 
```
A = [5, 4, 1, 3, 2, 0]  => res = [-1, -1, 4, -1, -1, -1]
```

### Brute Force: 
```python
def v5_brute_force(A): 
    n = len(A) 
    res = [-1] * n 
    for i in range(n): 
        j = i + 1
        while j < n and A[j] > A[i]: 
            res[i] = j 
            j += 1
    return res 
```
### With technique
```python
def v5_adv(A): 
    n = len(A)
    res = [-1] * n 
    stack = [] 
    for i in range(n): 
        while stack and A[stack[-1]] > A[i]: 
            idx = stack.pop() 
            if i - 1 > idx: 
                res[idx] = i - 1
        stack.append(i)
    return res 
```

