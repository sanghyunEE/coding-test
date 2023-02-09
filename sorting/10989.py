#계수정렬 써야함
import sys

n = int(input())
array = [0] * 10000

input = sys.stdin.readline
for _ in range(n):
    num = int(input())
    array[num - 1] += 1

for i in range(10000):
    if array[i] != 0:
        for j in range(array[i]):
            print(i+1)