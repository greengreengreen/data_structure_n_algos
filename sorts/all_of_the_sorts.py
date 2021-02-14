import random
import numpy as np 

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
    print(arr)

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
    print(arr)

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
    print(arr)

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

def bubble_sort(arr):
    def exchange(cnt): 
        for i in range(1, cnt): 
            if arr[i] < arr[i-1]: 
                arr[i], arr[i-1] = arr[i-1], arr[i]
    n = len(arr)
    for i in range(n, 0, -1): 
        exchange(i)
    print(arr)

def selection_sort(arr): 
    n = len(arr)
    def exchange(start): 
        for i in range(start+1, n): 
            if  arr[i] < arr[start]: 
                arr[i], arr[start] = arr[start], arr[i] 
    for i in range(n-1): 
        exchange(i)
    print(arr)

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

def pigeonhole_sort(arr): 
    min_val = min(arr)
    max_val = max(arr)
    l = max_val - min_val + 1
    pigeonhole = [[] for i in range(l)]
    for val in arr: 
        idx = val - min_val 
        pigeonhole[idx].append(val)
    i = 0
    for vals in pigeonhole: 
        for val in vals: 
            arr[i] = val 
            i += 1
    print(arr)
    
if __name__ == "__main__":
    arr = list(np.random.randint(-100, 100, 8)) 
    print(arr)
    print("quick sort")
    quick_sort_iter(arr[:])
    quick_sort_rcur(arr[:])
    print("heap sort")
    heap_sort(arr[:])
    print("merge sort")
    print(merge_sort_rcur(arr))
    print(merge_sort_iter(arr))
    print("bubble sort")
    bubble_sort(arr)
    print("selection sort")
    selection_sort(arr)
    print("insertion sort")
    insertion_sort(arr)

    # arr = list(np.random.randint(121, 130, 20))
    # print(arr)
    # print("pigeonhole sort")
    # pigeonhole_sort(arr[:])

