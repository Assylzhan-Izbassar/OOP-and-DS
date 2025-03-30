"""
Task 1
"""
def binary_search_nearest(a, p):
    l, r = 0, len(a) - 1
    res = -1

    while l <= r:
        mid = (l + r) // 2

        if a[mid] == p:
            return mid
        elif a[mid] < p:
            l = mid + 1
        else:
            r = mid - 1

        res = mid

    return res

arr = [1, 3, 5, 8, 10, 15]
target = 7

idx = binary_search_nearest(arr, target)

print(arr[idx])


"""
Task 2
"""
import bisect

def binary_search_right(a, p):
    l, r = 0, len(a) - 1
    res = []

    while l <= r:
        mid = (l + r) // 2
        if a[mid] <= p:
            if a[mid] == p:
                res.append(mid)
            l = mid + 1
        else:
            r = mid - 1

    return res


arr = [1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 7]
L, R = 5, 7

if (L >= R):
    print(-1, -1)
else:
    idx_l = binary_search_right(arr, L)
    idx_r = binary_search_right(arr, R)

    print(idx_l)
    print(idx_r)

    # idx_l = bisect.bisect_left(arr, L)
    # idx_r = bisect.bisect_right(arr, R)

    # print(idx_l, idx_r - 1)