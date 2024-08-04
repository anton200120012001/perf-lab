import sys
import math

if len(sys.argv) != 2:
        print("ERROR. How to run: python task4.py PATH_TO_FILE")
        sys.exit(1)

f1 = sys.argv[1]
with open(f1, 'r') as file:
    arr = list(map(int, file.read().strip().split()))

result_digit = math.ceil((max(arr))/2)
count = 0
for id, i in enumerate(arr):
    while i != result_digit:
        if i < result_digit:
            i += 1
            count += 1
        elif i > result_digit:
             i -= 1
             count += 1
        else:
            arr[id] = i

print('Result = ', count)
