n = 5
arr = [5, 3, 2, 4, 1]

count = 0

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            count += 1

print(count)