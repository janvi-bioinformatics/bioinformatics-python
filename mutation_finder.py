
dna1 = input("Enter DNA sequence:").upper()
dna2 = input("Enter DNA sequencs:").upper()

for i in range(len(dna1)):
	
	if dna1[i] != dna2[i]: 
	     print("Mutation at position", i+1, ":", dna1[i], "->", dna2[i])