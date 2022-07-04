# 1차 풀이
A, B, V = map(int, input().split())
result = 0
count = 0

while result >= V:
    if result + A >= V:
        count += 1
        break
    else:
        result += (A-B)
        count += 1
print(count)

# 2차 풀이
A,B,V = map(int, input().split())

if (V-B) % (A-B) == 0 :
    print((V-B) // (A-B))
else :
    print(((V-B) // (A-B)) +1)

#달팽이는 하루에 A-B 만큼 올라간다
#달팽이가 올라가야하는 길이는 V-B 다. (정상에 올라간 후에는 미끄러지지 않기 때문에 V만큼을 줄여야한다.)
#올라가야 하는 길이 (V-B) 를 하루에 올라가는 길이 (A-B) 로 나눈다
#나머지가 0이 아니라면 하루가 더 필요한 것으로 보고 +1을 해준다