s = input()

array = []

for i in range(len(s)):
    array.append(s[i:])

for i in sorted(array):
    print(i)