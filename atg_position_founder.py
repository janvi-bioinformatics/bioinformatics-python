dna = input("Enter DNA sequence:").upper()

for i in range(len(dna)-2):
	
	if dna[i:i+3] == "ATG":
		print("ATG found at position:", i+1)