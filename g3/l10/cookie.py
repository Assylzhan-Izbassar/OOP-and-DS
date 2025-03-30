def bubble_sort_2(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

g = [2, 1, 3, 1]
s = [1, 1]

n = len(g)
m = len(s)
child = 0
# marked = [False] * m

children = [False] * n

for i in range(m):
    for j in range(n):
        if children[j] == False and s[i] >= g[j]:
            child += 1
            children[j] = True
            continue

# for i in range(n):
#     for j in range(m):
#         if marked[j] == False and s[j] >= g[i]:
#             child += 1
#             marked[j] = True
#             continue

print(child)


bubble_sort_2(g)
bubble_sort_2(s)

ch = 0
co = 0

while ch < len(g) and co < len(s):
    if g[ch] <= s[co]:
        ch += 1
    co += 1

print(ch)

