cnt = int(input())

board = [[0] * 100 for _ in range(100)]

for _ in range(cnt):
    left, down = map(int, input().split())

    row = down - 10
    for i in range(10):
        for j in range(10):
            board[row][left + j] = 1
        row += 1

result = 0
for i in board:
    for j in i:
        if j == 1:
            result += 1
print(result)
