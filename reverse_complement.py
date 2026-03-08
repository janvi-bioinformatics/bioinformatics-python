
00dna = input("Enter DNA sequence").upper()
  
dna = dna.replace("A","t")
dna = dna.replace("T","a")
dna = dna.replace("G","c")
dna = dna.replace("C","g")
 
complement = dna.upper()
 
reverse_complement = complement[::-1]
 
print("Reverse Complement:", reverse_complement)