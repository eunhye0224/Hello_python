# 1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.
# 연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.

# 첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.

# 첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.

play = list(map(int,input().split()))

if play == list(range(1,9)):
    print('ascending')
elif play == list(range(8,0,-1)):
    print('descending')
else:
    print('mixed')
