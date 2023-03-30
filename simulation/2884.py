h, m = map(int, input().split())

if m - 45 < 0:
    if h - 1 < 0:
        print(23, 60 + (m - 45))
    else:
        print(h - 1, 60 + (m - 45))
else:
    m = m - 45
    print(h, m)