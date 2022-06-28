# 1차 풀이
X = int(input())
result=1

while result > X:
    result += (result+1)

# 2차 풀이
X = int(input())
line = 1
while X>line:
    X-=line
    line+=1
if line%2==0:
    a=X
    b=line-X+1
else:
    a=line-X+1
    b=X

print(a, '/', b, sep='')

# 도저히 아이디어가 떠오르지 않았음.
# 대각선 줄 별로 나눠서 해야. 