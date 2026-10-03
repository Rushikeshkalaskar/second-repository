arr = [10, 21, 32, 43, 54]

count = 0

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        count = count + 1

print(count)