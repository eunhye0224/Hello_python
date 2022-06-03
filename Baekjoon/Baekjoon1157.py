a = input().upper()
letterCnt = {}
for i in a :
    if i in letterCnt.keys():#dict키값들을 가져옴
        letterCnt[i]+=1
    else:
        letterCnt[i]=1
maxCount = 0
for k, v in letterCnt.items():#items 키벨류 셋트셋트
    if maxCount < v:
        answer = k
        maxCount = v
    elif maxCount == v:
        answer = '?'
print(answer)