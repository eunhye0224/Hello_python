s = 'TACCAATTGCAGCAGGGGGCAACCACACTTGTAGCCTGCTCTGCTGGCGGTTCGGTTATAAACATTATGAACGTCTCAAAACACCCGTGCGAGGCAACAGAAACGGGATACGGGGAACCCATTTCAACGCAGTCCAATCTGAGGAGACCCAGCGTAAGCCGGCGGCTGGGTTCGGTATACAAGTTTGACCCCATTACCATAGCTAATGTCCGGGACATGCGCACTCGGCGTTTCTTCTGACTCGACCCTACCACTTGAAGCTCATGAGATATCTAAACCACACTTATTAGTCGGTCGGGTGCCTATCAAGTGGTCTAGATGGTTCTCTGTCTTTAGAGCATCCTGGCGGCGGCAAGAACATCATATACACTAGGGCAACATCCGTAGTACATATGCATGGGACCTATGGAATTCGTTTTGTCGTGGAAACGACTTGATTCTATGCAAGTTTGACCTGCGACTGGGAGTAGCACCCAATTGCGGCTACTCCGGGTTGGCGCTGGTCACGTATCTGTGTAGCATTGTTGCATTCTTCACCGAGTAAAAACCAACGTCCCAGGTACTAATGACAGACACGACGTGAAATCTGTGTGTAGCGACACAATCCCACTTGAATACAGGTAAGCGATGAAAATGCGCTCGCGGAAGAATAACCACATTCCGGCTTATCTCGAGTTGCACTCGTGCATCAAGTGAAAACGTTAGATCCCGTCCTGTCGTCTCGCGGTGTACGGGGCCTTAGCTTAAATTTCACACACGGTCCCTCTTTTTTTCTCAATAACTAACGAGTGCGACTGTACGTTGGAGCTGGCGCCGCGCGAGTCGTTTTAACCGCGCAAAGCGGTAACGGTGCTTTGTAACCTTCGTCGACCAGTGGCTGCTGCTGGACGACACCGTAGCCAGTCCTCTCTAACCTCCGGTCGGGGGCACTAACTAGCCCTTTACTCAATTCAT'

new = ''
for i in range(len(s)):
    if s[i] == 'T':
        new += 'U'
    else:
        new += s[i]

print(new)


# S = s.split() 이렇게하면 리스트가 되버려서 S[i]에 사용할 수 없대