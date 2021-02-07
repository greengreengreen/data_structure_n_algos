def baseForm(A): 
    n = len(A)
    res = [[] for i in range(n)] 
    for i in range(n): 
        for j in range(i+1, n): 
            if A[j] > A[i]: 
                res[i].append(j) 
    return res 

def v1_brute_force(A): 
    n = len(A)
    res = [-1] * n 
    for i in range(n): 
        for j in range(i+1, n): 
            if A[j] > A[i]:
                if res[i] == -1 or A[res[i]] < A[j]: 
                    res[i] = j 
    return res

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

# Vanilla form + for all the eligible js of index i, find the j such that A[j] the largest one

def v2_brute_force(A):
    n = len(A)
    res = [-1] * n
    for i in range(n):
        for j in range(i, n):
            if A[j] > A[i]:
                if res[i] == -1 or A[res[i]] > A[j]:
                    res[i] = j
    return res

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


def v3_brute_force(A): 
    n = len(A)
    res = [-1] * n 
    for i in range(n): 
        for j in range(n-1, i, -1): 
            if A[j] > A[i]: 
                res[i] = j 
                break 
    return res 

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
        if l < len(arr): res[i] = arr[l]
        if (not arr) or (A[arr[-1]] < A[i]): 
            arr.append(i)
    return res


def v4_brute_force(A): 
    n = len(A)
    res = [-1] * n 
    for i in range(n): 
        for j in range(i+1, n): 
            if A[j] > A[i]: 
                res[i] = j 
                break 
    return res 

def v4_adv(A): 
    n = len(A)
    res = [-1] * n
    stack = []
    for j in range(n): 
        while stack and A[stack[-1]] < A[j]: 
            res[stack.pop()] = j
        stack.append(j)
    return res

def v5_brute_force(A): 
    n = len(A) 
    res = [-1] * n 
    for i in range(n): 
        j = i + 1
        while j < n and A[j] > A[i]: 
            res[i] = j 
            j += 1
    return res 

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

if __name__ == "__main__": 
    A = [1, 6, 2, 7, 8, 0]
    C = [1, 6, 2, 8, 7, 0]
    B = [5, 0, 2, 1, 3, 4]
    D = [5, 4, 1, 3, 2, 0]
    # Vanilla form: Given an array A, for each element at index i, find eligible indexes j such that A[i] < A[j] and i < j.
    print("vanilla form")
    print(baseForm(A))
    print(baseForm(B))
    # Variant1: Vanilla form + for all the eligible js of index i, find the j such that A[j] the largest one
    print("Variant1")
    print(v1_brute_force(A))
    print(v1_adv(A))
    print(v1_brute_force(B))
    print(v1_adv(B))
    # Variant2: Vanilla form + for all the eligible js of index i, find the j such that A[j] the smallest one.
    print("Variant2")
    print(v2_brute_force(A))
    print(v2_adv_tmp(A))
    print(v2_adv(A))
    print(v2_brute_force(B))
    print(v2_adv_tmp(B))
    print(v2_adv(B))
    # Variant3: Vanilla form + for all the eligible js of index i, find the j such that j is the largest.
    print("Variant3")
    print(v3_brute_force(C))
    print(v3_adv(C))
    print(v3_brute_force(D))
    print(v3_adv(D))
    # Variant4: Vanilla form + for all the eligible js of index i, find the j such that j is the smallest.
    print("Variant4")
    print(v4_brute_force(C))
    print(v4_adv(C))
    print(v4_brute_force(D))
    print(v4_adv(D))
    # Variant5: Vanilla form + for all the eligible js of index i, find the largest j such that any element between[i+1, j] is larger than A[i].
    print("Variant5")
    print(v5_brute_force(C))
    print(v5_adv(C))
    print(v5_brute_force(D))
    print(v5_adv(D))
