from itertools import permutations

n = int(input())

words = []
for _ in range(n):
    words.append(input())

words.sort(key= lambda x: len(x), reverse= True)

temp = ''
for word in words:
    temp += word

alpha = set(temp)
value = list(range(9, 9 - len(alpha), -1))
# print(value)
perm = list(permutations(value, len(alpha)))

# print(alpha)
# print(perm)


result = -1
for p in perm:
    dict_word = {}
    for a, i in zip(alpha, p):
        dict_word[a] = i
    # print(dict_word)

    current = 0
    for w in words:
        jari = 0
        for j in range(len(w) - 1, -1, -1):
            # print(j)
            # print(dict_word[w[j]] * (10 ** jari))
            current += dict_word[w[j]] * (10 ** jari)
            jari += 1
    # print(current)
    if result < current:
        result = current

print(result)

# for i in alpha:
#     dict_word = {}
#     dict_word[i] = 

# print(dict_word)

