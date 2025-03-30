arr = [1, 3, 5, 8, 10, 15]
target = 7

l, r = 0, len(arr) - 1
result = -1

while l <= r:
    mid = (l + r) // 2
    if arr[mid] == target:
        result = mid
    elif arr[mid] > target:
        r = mid - 1
    else:
        l = mid + 1

    result = mid

print(arr[result])

