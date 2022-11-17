#Reading and Writing
f = open("rosalind_ini5.txt", "r")
output = open("output_INI5.txt", "w")
i = 1

for line in f.readlines():
	if i % 2 == 0:
		output.write(line)
	i = i + 1


