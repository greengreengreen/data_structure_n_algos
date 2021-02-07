def basic(A): 
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

def v2_brute_force(A): 
    n = len(A) 
    res = [-1] * n 
    for i in range(n): 
        for j in range(i, n): 
            if A[j] > A[i]:
                if res[i] == -1 or A[res[i]] > A[j]:
                    res[i] = j 
    return res


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
    for i in range(n): 
        while stack and A[stack[-1]] < A[i]: 
            res[stack.pop()] = i 
        stack.append(i)
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
    for i in range(n): 
        while stack and A[stack[-1]] > A[i]: 
            idx = stack.pop() 
            if i - 1 > idx: 
                res[idx] = i - 1
        stack.append(i)
    return res 


if __name__ == "__main__": 
    A = [1, 6, 2, 7, 8, 0]
    A = [1, 6, 2, 8, 7, 0]
    # print(variant1(A))
    B = [5, 0, 2, 1, 3, 4]
    B = [5, 4, 1, 3, 2, 0]
    # print(variant1(B))
    # print(v3_brute_force(A))
    # print(v3_adv(A))
    print(v5_brute_force(A))
    print(v5_adv(A))

