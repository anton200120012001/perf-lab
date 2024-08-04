# соответствия ответов:
# 0 - точка лежит на окружности
# 1 - точка внутри
# 2 - точка снаружи.
import sys

if len(sys.argv) != 3:
        print("ERROR. How to run: python task2.py PATH_TO_FILE1 PATH_TO_FILE2")
        sys.exit(1)

f1 = sys.argv[1]
f2 = sys.argv[2]

with open(f1, 'r') as file:
    data = file.read().strip().split()
    x = float(data[0])
    y = float(data[1])
    r = float(data[2])

with open(f2, 'r') as file:
    for line in file:
        x1, y1 = map(float, line.strip().split())
        temp=(x1-x)**2 + (y1-y)**2
        if temp < r**2:
            print("1")
        elif temp == r**2:
            print("0")
        else:
            print("2")

