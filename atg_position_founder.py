dna = input("Enter DNA sequence: ").upper()
count = 0

for i in range(len(dna)-2):

    codon = dna[i:i+3]

    if codon == "ATG":
        print("Start codon at position:", i+1)
        count += 1

print("Total ATG found:", count)
