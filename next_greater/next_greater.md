# Next Greater Problem And Its Homies

> You got a new friend. well. I got homies. — Heartless by Kanye West

It is very common to see the next greater element problems these days. In this article, I will go from solving the vanilla form of this problem to analyzing and illustrating some of its variants. I will talk about when to sort, how to traverse (from left or right), and when we will need an auxiliary array. 

## Overview
* [Vanilla form](#vanilla-form): Given an array A, for each element at index i, find eligible indexes j such that A[i] < A[j] and i < j. 
* [Variant1](#variant1): Vanilla form + for all the eligible js of index i, find the j such that A[j] the largest one
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
A  =  [1,  6,  2,  7,  8,  0]
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
Yes. We can make it O(nlogn). Of course, O(nlogn) didn’t count the time to copy indexes into the result array. 
There are several ways to achieve this. Since the base form optimization is not the focus of this post, I will create another post for it. 

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
This problem is asking for the index of the largest element between [i+1, n-1] for each index i in A. Let's traverse from right to left and maintain the index of the largest element as maxidx. In this way, at index i, if A[i] > A[maxidx], it means no element in [i+1, n-1] is greater than A[i]. Hence res[i] = -1. A[i] is the largest element between [i, n-1] and maxidx should be updated to i. if A[i] <= A[maxidx], then A[maxidx] is the largest element so far. res[i] = i. 

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
### With technique Sorting O(nlogn)
My first intuition is to traverse A from right to left and add all the elements I have looped into a sorted array arr. To get res[i], do a binary search for arr. Since arr is increasing in values, I just need to find the smallest element greater than A[i]. After that, I will need to insert A[i] into arr, which takes O(n) time. 

```python
def v2_adv_tmp(A): 
    n = len(A)
    res = [-1] * n 
    arr = []
    for i in range(n-1, -1, -1): 
        l, r = 0, len(arr)
        while l < r: 
            m = l + (r-l)//2 
            if A[arr[m]] > A[i]: r = m 
            else: l = m+1 
        if l < len(arr): res[i] = arr[l] 
        arr.insert(l, i)
    return res 
```

Can we do better? </br>
Yes. </br>
The most unpleasant part of the above solution is that the insert operation takes O(n) time. </br>
Is there a way we can get rid of it? </br>
Instead of sorting and inserting while traversing, let's sort A in one pass and store it into arr. Hence, if we traverse arr, 
arr[i+1] is always the smallest possible value which is greater than arr[i]. The only thing criteria to take care of is index. Remember j needs to be greater than i. </br>
How can we satisfy the index? </br>
By storing all the elements we have looped so far into a stack. This stack should be storing the actual index that the value locates in A. We want to make sure this stack stores 1. decreasing indexes  2. whose corresponding value in A is increasing.
Hence, when we encounter a new (num, j) in arr, before we can append it to stack, we need to pop out all the indexes in the stack which are smaller than j. The indexes we popped out from stack are the corresponding is for this current index j which we are trying to append in the stack. In this way, we successfully get the i, j pairs we desire. </br>

```python 
def v2_adv(A):
    arr = sorted([(num, i) for i, num in enumerate(A)])
    n = len(A)
    res = [-1] * n
    stack = []
    for num, j in arr:
        while stack and stack[-1] < j:
            res[stack.pop()] = j
        stack.append(j)
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
### With technique Binary Seach O(nlogn)
This problem asks for the rightmost j that satisfies A[j] > A[i] for each i. A[j] does not have to be the largest among all the js. To achieve this, let's again loop from the right to left. At the same time, we maintain an auxiliary array arr, which stores indexes which are sorted in [A[idx], idx]. </br>
Feels the same as v2_adv_tmp which we discussed in variant 2, right? <br>
The only difference is that we are freed from the insert operation in this problem. If we encounter i in A, and there are already elements in arr which are greater than A[i], then there's no need for us to insert it into arr. </br>

```python
def v3_adv(A): 
    n = len(A)
    res = [-1] * n 
    arr = []
    for i in range(n-1, -1, -1): 
        l, r = 0, len(arr)
        while l < r: 
            m = l + (r-l)//2
            if A[arr[m]] <= A[i]: l = m + 1
            else: r = m
        if l < len(q): res[i] = arr[l]
        if (not arr) or (A[arr[-1]] < A[i]): 
            arr.append(i)
    return res
```
## Variant4
>Vanilla form + for all the eligible js of index i, find the j such that j is the smallest.
### Problem statement: 
Given an array A, for each element at index i, among all the eligible indexes j such that A[i] < A[j] and i < j, find the j such that j is the smallest index possible. 
### Examples: 
Example1: 
```
A       =  [1,  6,  2,  8,  7,  0]
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

### Brute Force O(n^2)
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
### With technique Monotonic Stack O(n)
The problem asks for the index of the closest element which is greater than A[i] for each index i in A. Let's maintain a stack, which has increasing indexes and decreasing values. It means that the values' of indexes that the stack stores are decreasing while indexes themselves are increasing. </br>
Why? </br>
If we encounter an index j, whose value A[j] is greater than any elements in the stack, then we have found all the j which satisfies all the is in the stack. Because we loop from left to right, all the is are smaller than j. 
So, before we append j into the stack, we pop out all the eligible is in the stack which has A[i] < A[j]. This way, we get all the i, j pairs and maintains the monotonic stack. </br>

```python
def v4_adv(A): 
    n = len(A)
    res = [-1] * n
    stack = []
    for j in range(n): 
        while stack and A[stack[-1]] < A[j]: 
            res[stack.pop()] = j
        stack.append(j)
    return res
```

## Variant5
>Vanilla form + for all the eligible js of index i, find the largest j such that any element between [i+1, j] is larger than A[i].
### Problem statement: 
Given an array A, for each element at index i, among all the eligible indexes j such that A[i] < A[j] and i < j, find the largest j such that any element between [i+1, j] is larger than A[i].
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

### Brute Force O(n^2) 
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
### With technique Montonic stack O(n)
So any element between [i+1, j] has to be greater than A[i]. A[j+1] is the first element in A[i+1:] to be smaller than A[i]. Let's focus on find the A[j+1]. Recall in variant4, we were finding the first element in A[i+1:] to be greater than A[i]. We take the prototype in variant4 and use it to find the first smaller element's index. </br>
How should we change solutions in variant4? </br>
In variant4, we had a stack increasing in index and decreasing in values. 
Let's change it to maintaining a stack that is increasing in index but increasing in values. 
How does the new stack work?
If we encounter an index j, whose value A[j] is smaller than any elements in the stack, then we have found the j which satisfies all the is in the stack. Because we loop from left to right, all the is are smaller than j. 
So, before we append j into stack, we pop out all the eligible is in stack which has A[i] > A[j]. This way, we get all the i, j pairs and maintains the monotonic stack. Note that we actually put j-1 into the res as it is A[j] > A[i].</br> 

```python
def v5_adv(A): 
    n = len(A)
    res = [-1] * n 
    stack = [] 
    for j in range(n): 
        while stack and A[stack[-1]] > A[j]: 
            idx = stack.pop() 
            if j - 1 > idx: 
                res[idx] = j - 1
        stack.append(j)
    return res 
```

## Conclusion 

At this point, since you have seen the next greater problem and its five homies, you are already very familiar with the next greater patterns. The trick is to decide where to traverse (left or right), when to sort (during traverse or before), how to sort(index increasing or decreasing, value increasing or decreasing), what to store (use a stack or array?). </br>

In addition, I found some problems where you can test your knowledge. They are not exactly the same problem, but hopefully, you can feel how they are bonded when practicing. 
1. Variant1: [LC 42 Trapping Water](https://leetcode.com/problems/trapping-rain-water/)
2. Variant2: [LC 975 Odd Even Jump](https://leetcode.com/problems/odd-even-jump/)
3. Variant3: [LC 962 Maximum Width Ramp](https://leetcode.com/problems/maximum-width-ramp/)
4. Variant 4+5: [LC 901 Online Stock Span](https://leetcode.com/problems/online-stock-span/)
