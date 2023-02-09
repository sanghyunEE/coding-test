n = int(input())

b = list(map(int, input().split())) # 길이
a = list(map(int, input().split())) # 주유비
a.pop()

result = 0
for i in range(n-1):
    if i == 0:
        result += a[i] * b[i]
    elif a[i] > a[i-1]:
        if (a[i] * b[i] + a[i-1] * b[i-1] < a[i-1] * (b[i] + b[i-1])):
            result += a[i] * b[i]
        else:
            result += -(a[i-1] * b[i-1]) + a[i-1] * (b[i] + b[i-1])
    else:
        result += a[i] * b[i]
print(result)

# https://reliablecho-programming.tistory.com/59
# 숏코딩 참고