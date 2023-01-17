n = int(input()) # 설탕 무게 input

result = 0 # 배달하는 봉지의 최소 개수

# 한 번의 반복마다 3을 하나씩 빼가면서 5의 배수가 될 때까지 만들기
while True:
    if n % 5 == 0: # 5의 배수인지 체크
        result += n // 5
        break
    n -= 3
    if n < 0:
        result = -1
        break
    elif n == 0:
        result += 1
        break
    else:
        result += 1
print(result)