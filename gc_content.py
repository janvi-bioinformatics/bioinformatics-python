
dna = input("Enter DNA sequence")
length = len(dna)

G = dna.count("G")
C = dna.count("C")

gc_content = ( (G+C) / len(dna) ) * 100

print("DNA Length:", length)
print("GC Content:", gc_content, "%")