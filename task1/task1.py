import sys

if len(sys.argv) != 3:
        print("ERROR. How to run: python task1.py n m")
        sys.exit(1)

n = int(sys.argv[1])
m = int(sys.argv[2])
i = 1
print('Result:')
while True:
    print(i, end='')
    i = (i + m - 2) % n + 1
    if i == 1:
        break
print('')