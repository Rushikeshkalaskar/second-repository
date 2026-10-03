arr = [10, 0, 20, 0, 30, 40]

count = 0

for i in range(len(arr)):
    if arr[i] == 0:
        count = count + 1

print(count)