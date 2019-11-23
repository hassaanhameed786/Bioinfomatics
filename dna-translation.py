import sys

file = open('dna.txt', 'r')
dna = file.read()
valid_dna = ["a", "c", "g", "t", "A", "C", "G", "T"]

for i in range(0, len(dna)-1):
    if dna[i] in valid_dna:
        continue
    else:
        print "The DNA sequence is not valid"
        sys.exit()



print "DNA: "
print dna

mrna = ""

for i in dna:
    if i == "T" or i == "t":
        mrna += "U"
    else:
        mrna += i.upper()


print "mRNA: "
print mrna

# codon table
codon = {"UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V",
           "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
           "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
           "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
           "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
           "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
           "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
           "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
           "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D",
           "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
           "UAA" : "STOP", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
           "UAG" : "STOP", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
           "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G",
           "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
           "UGA" : "STOP", "CGA" : "R", "AGA" : "R", "GGA" : "G",
           "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" 
           }

protein_string = ""

# Generate protein string
for i in range(0, len(mrna)-(3+len(mrna)%3), 3):
        protein_string += codon[mrna[i:i+3]]
        protein_string += "-"

# Print the protein string
print "Protein Strings: \n", protein_string