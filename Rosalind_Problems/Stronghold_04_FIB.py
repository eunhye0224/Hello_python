#피보나치
n=32
k=4
rabbit = []
# print(range(n))
for i in range(n):
    if i <= 1:
        rabbit.append(1)
    elif i == 2:
        rabbit.append(1+k)
    elif i >= 3:
        # x = 0
        # x += rabbit[i-1] # -> +=방향성 잘 정리하기!!!
        # rabbit[i-1] += x ->이렇게 하면 자꾸 0으로 됨
        # print(rabbit[i-1], type(rabbit[i-1]))
        # y=0
        # y+=(x-1)*k+1
        # rabbit.append(y)
        rabbit.append(rabbit[i-2]*k+rabbit[i-1])
print(rabbit[-1])

#개념정리 : 피보나치 수열 / list추가는 append / += 방향성 정리!할것


def fibo(n,k):
    rabbit = []
    for i in range(n):
        if i <= 1:
            rabbit.append(1)
        elif i == 2:
            rabbit.append(1+k)
        elif i >= 3:
            rabbit.append(rabbit[i-2]*k+rabbit[i-1])
    return rabbit[-1]

print(fibo(32,4))



