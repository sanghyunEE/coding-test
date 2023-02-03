n, m = map(int, input().split())

trees = list(map(int, input().split()))

start = 0
end = max(trees)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in trees:
        if i - mid > 0:
            total += i - mid
    
    if total > m: # 절단기의 높이를 높여라 (오른쪽 탐색)
        result = mid
        start = mid + 1
    elif total == m:
        result = mid
        break
    else: # 절단기의 높이를 낮춰라 (왼쪽 탐색)
        end = mid - 1

print(result)

# python 3 로 제출 했는데 시간초과 난다 -> 아마 14 15 번 라인에서 계산하는게 
# 많아서 그런듯 -> total이 m 보다 넘어 버리면 그냥 바로 end = mid - 1해주고 break 걸어보자
# 저기서 계산이 거의 1,000,000 진행되기 때문임 ㅇㅇ

