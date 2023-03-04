n = int(input())
result = 0
for _ in range(n):
    word = input()

    alpha = 'abcdefghijklmnopqrstuvwxyz'
    table = {}
    for i in alpha:
        table[i] = 0
    flag = 0
    prev = word[0]
    for i in range(1, len(word)):
        
        if prev == word[i]:
            prev = word[i]
            continue
        else:
            if table[prev] > 0:
                flag = 1
                break
            else:
                table[prev] += 1
                prev = word[i]
    if table[word[-1]] > 0:
        flag = 1
    else:
        table[word[-1]] += 1

    if flag == 0: result += 1
    
print(result)