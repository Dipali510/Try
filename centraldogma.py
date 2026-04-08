# Central Dogma of Molecular Biology dna to rna to protein
# DNA to RNA

dna="ATGATG"
rna=dna.replace("T","U")
print(rna)

# RNA to Protein
protein=""
comp_codon={"AUG":"M","UUU":"F","UUC":"F"}
for i in range(0,len(rna),3):
    codon=rna[i:i+3]
    protein+=comp_codon[codon]
print(protein)