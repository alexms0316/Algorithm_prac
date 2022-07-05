# 1차 풀이
N = int(input())
count = 0

while N >= 5:
    N -= 5
    count += 1
    continue
if N % 3 == 0:
    print(count + 1)
else:
    print(-1)

# 2차 풀이
N = int(input())
count = 0

while N >= 0:
    if N % 5 == 0:
        count += (N // 5)
        print(count)
        break
    N -= 3
    count += 1
else:
    print(-1)
