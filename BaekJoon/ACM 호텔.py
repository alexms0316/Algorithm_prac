# 1차 풀이
T = int(input())
for i in range(1,T):
    def reservation():
        H, W, N = map(int, input().split())
        count = 0
        while H >= N:
            H -= N
            count += 1
            continue
        if count < 10 and count <= W:
            print(str(H) + '0' + str(count))
        elif count >= 10:
            print(str(H) + '' + str(count))
        elif count > W:
            print(str(H+1) + '' + str(count))
    reservation()

# 2차 풀이
# t = int(input())
# for i in range(t):
#     h, w, n = map(int, input().split())
#     num = n//h + 1
#     floor = n % h
#     if n % h == 0: 
#         num = n//h
#         floor = h
#     print(f'{floor*100+num}')