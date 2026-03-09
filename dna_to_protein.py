
dna = input("Enter DNA sequence:").upper()

codon_table = { 
"ATG": "M",
"TTT": "F",
"GCT": "A"
}

for i in range(0, len(dna), 3):
	codon = dna[i:i+3]
	
	if codon in codon_table:
		print(codon_table[codon], end=" ")