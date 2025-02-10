def bubble_sort(lst):
    length = len(lst)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j],lst[j + 1] = lst[j + 1], lst[j]
m = [0,9,8,3,5,-5]
bubble_sort(m)
print(m)

def mege_sort(arr):
    if len(arr) == 1:
        return
    mid = len(arr) // 2
    L = arr[:mid]
    r = arr[mid:]
    mege_sort(L)
    mege_sort(r)

    i = j = k = 0
    while i < len(L) and j < len(r):
        if L[i] < r[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1

lse = [0,8,6,3,1]
mege_sort(lse)
print(lse)