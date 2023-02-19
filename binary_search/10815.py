n = int(input())
n_arr = list(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

n_arr.sort()

# index 반환
def binary_search(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            return True
    return False

result = [0 for _ in range(m)]
for i in range(m): # o(N)
    if binary_search(n_arr, 0, n-1, m_arr[i]): # o(logN)
        result[i] = 1
# 총 O(NlogN) 500,000에 대해서 가능
for i in result:
    print(i, end=' ')