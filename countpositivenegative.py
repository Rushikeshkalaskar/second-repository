arr = [10, -20, 30, -40, 50]

positive = 0
negative = 0

for i in range(len(arr)):
    if arr[i] > 0:
        positive = positive + 1
    elif arr[i] < 0:
        negative = negative + 1

print(positive)
print(negative)