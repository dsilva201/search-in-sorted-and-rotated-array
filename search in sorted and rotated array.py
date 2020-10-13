def searchkey(arr, s, e, k):
    if s > e:
        return -1
    mid = (s + e) // 2
    if arr[mid] == k:
        return mid
    if arr[s] <= arr[mid]:
        if k >= arr[s] and k <= arr[mid]:
            return searchkey(arr, s, mid-1, k)
        return searchkey(arr, mid+1, e, k)
    if k >= arr[mid] and k <= arr[mid]:
        return searchkey(arr, mid+1, e, k)
    return searchkey(arr, s, mid-1, k)
n = input("Enter Array:").split()
n = [int(i) for i in n]
k = int(input("Enter Key That You Want To Search:"))
b = searchkey(n, 0, len(n)-1, k)
print(b)