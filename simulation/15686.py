from itertools import combinations

n, m = map(int,input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

chicken = []
house = []
for i in range(n): # 최대 2500 번
    for j in range(n):
        if data[i][j] == 2:
            chicken.append((i, j))
        elif data[i][j] == 1:
            house.append((i, j))

comb_chicken = combinations(chicken, m) # 최대 1700번

result = int(1e9)
for comb in comb_chicken: # 1700
    temp = 0
    for h in house: # 100
        dist = 102
        for c in comb:
            dist = min(dist, abs(c[0] - h[0]) + abs(c[1] - h[1])) 
        temp += dist
    result = min(result, temp)

print(result)