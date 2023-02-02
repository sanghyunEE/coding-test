import sys

n = int(sys.stdin.readline())

array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

for i in array:
    print(i)

# https://coarmok.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%ACpython-%EB%B0%B1%EC%A4%80-2751%EB%B2%88-merge-sort