s = input()

number = []
minus = s.split('-')
for i in minus:
    temp = i.split('+')
    for j in temp:
        number.append(j)
# print(number)

sign = []
for i in s:
    if i == '-' or i == '+':
        sign.append(i)
# print(sign)

exp = number.copy()
for i in range(len(sign)):
    exp.insert(2*i+1, sign[i])
# print(exp)
# print(''.join(exp))

result = 9999999
for i in [0, 2, 4]:
    for j in range(i+2, len(exp)+2, 2):
        temp = exp.copy()
        temp.insert(i, '(')
        temp.insert(j, ')')
        result = min(result, eval(''.join(temp)))

print(result)