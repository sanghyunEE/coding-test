n = int(input()) # 사람의 수
times = list(map(int, input().split())) # 걸리는 시간

# times를 sort하기 (NlogN)
times.sort()

# 각 지점 별 소요 시간을 담을 리스트
sum_list = [0] * n
for i in range(n):
    if i == 0:
        sum_list[i] = times[i]    
    else:
        sum_list[i] = sum_list[i-1] + times[i]
print(sum(sum_list))


