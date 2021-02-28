import math

def binary_search_var1(arr, target): 
    # 1. Given an increasingly sorted array, return the first index which has value == target.
    n = len(arr)
    l, r = 0, n 
    while l < r: 
        m = l + (r-l)//2 
        if arr[m] >= target: r = m
        else: l = m + 1
    return l if l < n and arr[l] == target else -1 

def binary_search_var2(arr, target):
    # 2. Given a descreasingly sorted array, return the first index which has value == target.
    n = len(arr)
    l, r = 0, n 
    while l < r: 
        m = l + (r-l)//2 
        if arr[m] <= target: r = m 
        else: l = m + 1
    return l if l < n and arr[l] == target else -1 


def binary_search_var3(arr, target):
    # 3. Given a increasingly sorted array, return the last index which has value == target.
    n = len(arr)
    l, r = -1, n-1 
    while l < r: 
        m = l + math.ceil((r-l)/2)
        if arr[m] <= target: l = m 
        else: r = m - 1
    return r if r >= 0 and arr[r] == target else -1 

def binary_search_var4(arr, target):
    # 4. Given a descreasingly sorted array, return the last index which has value == target.
    n = len(arr)
    l, r = -1, n-1 
    while l < r: 
        m = l + math.ceil((r-l)/2)
        if arr[m] >= target: l = m 
        else: r = m-1 
    return r if r >= 0 and arr[r] == target else -1 

def binary_search_var5(arr, target):
    # 5. Given a increasingly sorted array, return the first index which has value > target.
    n = len(arr)
    l, r = 0, n 
    while l < r:
        m = l + (r-l)//2 
        if arr[m] > target: r = m 
        else: l = m + 1
    return l if l < n and arr[l] > target else -1 

def binary_search_var6(arr, target):
    # 6. Given a increasingly sorted array, return the first index which has value >= target.
    n = len(arr)
    l, r = 0, n 
    while l < r: 
        m = l + (r-l)//2 
        if arr[m] >= target: r = m 
        else: l = m + 1
    return l if l >= 0 and arr[l] >= target else -1 

def binary_search_var7(arr, target): 
    # 7. Given a descreasingly sorted array, return the last index which has value > target.
    n = len(arr)
    l, r = -1, n-1
    while l < r: 
        m = l + math.ceil((r-l)/2)
        if arr[m] > target: l = m 
        else: r = m - 1
    return r if r >= 0 and arr[r] > target else -1 


def binary_search_var8(arr, target):
    # 8. Given a descreasingly sorted array, return the last index which has value >= target.
    n = len(arr)
    l, r = -1, n-1 
    while l < r: 
        m = l + math.ceil((r-l)/2)
        if arr[m] >= target: l = m 
        else: r = m -1 
    return r if r >= 0 and arr[r] >= target else -1 

def binary_search_var9(arr, target): 
    # 9. Given a increasingly sorted array, return the last index which has value < target.
    n = len(arr)
    l, r = -1, n-1 
    while l < r: 
        m = l + math.ceil((r-l)/2)
        if arr[m] < target: l = m 
        else: r = m - 1
    return r if r >= 0 and arr[m] < target else -1

def binary_search_var10(arr, target): 
    # 10. Given a increasingly sorted array, return the last index which has value <= target.
    n = len(arr)
    l, r = -1, n-1 
    while l < r: 
        m = l + math.ceil((r-l)/2)
        if arr[m] <= target: l = m 
        else: r = m - 1
    return r if r >= 0 and arr[r] <= target else -1

def binary_search_var11(arr, target): 
    # 11. Given a descreasingly sorted array, return the first index which has value < target.
    n = len(arr) 
    l, r = 0, n
    while l < r: 
        m = l + (r-l)//2 
        if arr[m] < target: r = m 
        else: l = m + 1
    return l if l < n and arr[l] < target else -1 

def binary_search_var12(arr, target): 
    # 12. Given a descreasingly sorted array, return the first index which has value <= target.
    n = len(arr)
    l, r = 0, n 
    while l < r: 
        m = l + (r-l)//2 
        if arr[m] <= target: r = m 
        else: l = m + 1
    return l if l < n and arr[l] <= target else -1 

if __name__ == "__main__":
    arr_insc = [-1, 1, 3, 5, 6, 7, 7, 8, 8, 8, 10]
    arr_desc = [10, 8, 8, 8, 7, 7, 6, 5, 3, 1, -1]
    # 1. Given an increasingly sorted array, return the first index which has value == target.
    print("Given an increasingly sorted array, return the first index which has value == target.")
    print(binary_search_var1(arr_insc, 7))
    print(binary_search_var1(arr_insc, 11))
    # 2. Given a descreasingly sorted array, return the first index which has value == target.
    print("#" * 20)
    print("Given a descreasingly sorted array, return the first index which has value == target.")
    print(binary_search_var2(arr_desc, 8))
    print(binary_search_var2(arr_desc, 11))
    # 3. Given a increasingly sorted array, return the last index which has value == target.
    print("#" * 20)
    print("Given a increasingly sorted array, return the last index which has value == target.")
    print(binary_search_var3(arr_insc, 7))
    print(binary_search_var3(arr_insc, -1))
    # 4. Given a descreasingly sorted array, return the last index which has value == target.
    print("#" * 20)
    print("Given a descreasingly sorted array, return the last index which has value == target.")
    print(binary_search_var4(arr_desc, 8))
    print(binary_search_var4(arr_desc, -2))
    # 5. Given a increasingly sorted array, return the first index which has value > target.
    print("#" * 20)
    print("Given a increasingly sorted array, return the first index which has value > target.")
    print(binary_search_var5(arr_insc, 8))
    print(binary_search_var5(arr_insc, -12))
    # 6. Given a increasingly sorted array, return the first index which has value >= target.
    print("#" * 20)
    print("Given a increasingly sorted array, return the first index which has value >= target.")
    print(binary_search_var6(arr_insc, 8))
    print(binary_search_var6(arr_insc, 9))
    # 7. Given a descreasingly sorted array, return the last index which has value > target.
    print("#" * 20)
    print("Given a descreasingly sorted array, return the last index which has value > target.")
    print(binary_search_var7(arr_desc, 9))
    print(binary_search_var7(arr_desc, 6))
    # 8. Given a descreasingly sorted array, return the last index which has value >= target.
    print("#" * 20)
    print("Given a descreasingly sorted array, return the last index which has value >= target.")
    print(binary_search_var8(arr_desc, 9))
    print(binary_search_var8(arr_desc, 6))
    # 9. Given a increasingly sorted array, return the last index which has value < target.
    print("#" * 20)
    print("Given a increasingly sorted array, return the last index which has value < target.")
    print(binary_search_var9(arr_insc, 7))
    print(binary_search_var9(arr_insc, -2))
    # 10. Given a increasingly sorted array, return the last index which has value <= target.
    print("#" * 20)
    print("Given a increasingly sorted array, return the last index which has value <= target.")
    print(binary_search_var10(arr_insc, 7))
    print(binary_search_var10(arr_insc, 10))
    # 11. Given a descreasingly sorted array, return the first index which has value < target.
    print("#" * 20)
    print("Given a descreasingly sorted array, return the first index which has value < target.")
    print(binary_search_var11(arr_desc, 7))
    print(binary_search_var11(arr_desc, 12))
    # 12. Given a descreasingly sorted array, return the first index which has value <= target.
    print("#" * 20)
    print("Given a descreasingly sorted array, return the first index which has value <= target.")
    print(binary_search_var12(arr_desc, 7))
    print(binary_search_var12(arr_desc, 10))
