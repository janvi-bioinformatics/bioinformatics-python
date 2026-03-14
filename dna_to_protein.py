dna = input("Enter DNA sequence: ").upper()

codon_table = { 
"ATG": "M",
"TTT": "F",
"TTC": "F",
"GCC": "A",
"GCA": "A",
"GCG": "A",
"GCT": "A"
}

start = dna.find("ATG")

if start == -1:
    print("No start codon found")
else:
    protein = ""

    for i in range(start, len(dna)-2, 3):
        codon = dna[i:i+3]

        if codon in ["TAA","TAG","TGA"]:
            break

        if codon in codon_table:
            protein += codon_table[codon]
        else:
            protein += "?"

    print("Protein:", protein)
