# eval 을 쓰는 문제가 아님
s = input()

array = s.split('-')
result = 0
if len(array) >= 2: # - 기호가 있다는 뜻
    for i in range(len(array)):
        for j in array[i].split('+'):
            if i == 0:
                result += int(j)
            else:
                result -= int(j)
else: # - 기호가 없다는 뜻
    temp = s.split('+')
    for i in temp:
        result += int(i)
print(result)

# https://pacific-ocean.tistory.com/228



