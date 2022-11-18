#finding a motif in dna

s = 'GATATATGCATATACTT'
f = 'ATAT'
location = []

for i in range(s.find(f),len(s)):
    if s[i:i+4]==f:
        location.append(i+1)
    else:
        pass

print(location)
#이렇게 짜니까 리스트 형태로 프린트 되서 콤마를 지울 수 없음


S = 'TAGACATATATTACGTTTAGCTTGTTAGACATGTAGACATCCCGAATGCCTAGTAGACATTAGACATCGATCAGTAGACATGCAGAGCCCTTAGACATGGCTACCCTGCTAGACATGAACGGGAAGTTTAGACATTAGACATTGTAGACATCTAGACATCTTAGACATTCCTTAGACATCTAGACATCCACCTAGACATGGATAGACATATAGACATGTAGACATTAGACATTTTAGACATTAGACATGCGTAGACATTAGACATGTAGACATTAGACATATAGACATTAGACATGTTTAGACATTAGTTAGACATCACTAGACATTAGACATCTAAGCGTTAGACATCTAGACATTAGACATGTAGACATCACTAGACATAAGTTGTACCTACCTAGATTAGACATGCGCAGCCTATAGACATTCTACCCTTAGACATGGCCTAGACATTAGACATTAGACATCCTTTAGACATATTTAGACATTCCTAGACATGATAGACATTAGACATTAGACATGTAGACATGAAGAGACGGCATAGACATTTACGTAGACATAATTGTAGACATTGTGTAGACATGACTGCGTAGACATGTCTGATTAGACATGCCGGTTAGACATTAGTAGACATGCTAGACATTATAGACATCGGTAGTAACTAGACATCGAGGCATAGACATTAGACATTAGACATTTAGACATGGCACTAGACATTTAGACATTATAGACATTAGACATGTAGACATTTAGACATTACGTACTAGACATCCTTGTAGACATGTAGACATGCGGGGTTAGACATTCTGATATATAGACAT'
F = 'TAGACATTA'

Location = ''
#str형태로 해서 공백추가 해줌

for i in range(S.find(F),len(S)):
    if S[i:i+9]==F:
        Location+=str(i+1)+' '
    # else:
    #     pass

print(Location)


#다른 사람 코드

def find_motif(s,t):
    positions = ''
    for i in range(len(s)):
        if s[i] == t[0]:
            if s[i:i+len(t)] == t:
                positions += str(i+1)+' '
    return positions


with open('rosalind_subs.txt','r') as file:
    content = file.read()
DNA, subDNA = content.splitlines()
print(find_motif(DNA, subDNA))