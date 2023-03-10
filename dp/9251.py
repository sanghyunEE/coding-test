# 중요 !!
# 재귀로도 풀수있지만 시간초과 남
# 재귀의 중복부분을 제거하는 방법이 '동적 계획법'

first = list(input())
second = list(input())


def lcs(x, y):
    x, y = [' '] + x, [' '] + y
    m, n = len(x), len(y)

    c = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i][j - 1], c[i - 1][j])
    return c[m-1][n-1]
print(lcs(first, second))