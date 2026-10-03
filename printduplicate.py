arr = [10, 20, 10, 30, 20, 40]

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            print(arr[i])