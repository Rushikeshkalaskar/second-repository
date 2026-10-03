arr = [10, 50, 20, 40, 30]

largest = arr[0]
second = arr[0]

for i in range(len(arr)):
    if arr[i] > largest:
        second = largest
        largest = arr[i]
    elif arr[i] > second and arr[i] != largest:
        second = arr[i]

print(second)