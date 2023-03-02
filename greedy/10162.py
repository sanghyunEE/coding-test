t = int(input())

times = [300, 60, 10]
result = [0, 0, 0]

for i in range(3):
    if t // times[i] >= 1:
        result[i] = t // times[i]
        t = t % times[i]
if t > 0:
    print(-1)
else:
    print(*result)
        
