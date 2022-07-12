# 1차 풀이
n = int(input())
count = 0
num = count+1
number = 7+(6*(num-1))
while n < number:
    for i in range(num):   
        number = sum(number)
        count+=1
print(count)

# 2차 풀이
n = int(input())
nums = 1
count = 1
while n > nums:
    nums += (6 * count)
    count += 1
print(count)

# 왜 이렇게 복잡하게 생각한지 모르겠음.
# '+=' 를 왜 제대로 생각하지 못했는가 반성. 