gen_cod={
    'ATG': 'M',
    'TTA': '*',
    'TAG': '*',
}
seq=""
with open ("sample.fasta")as f:
    for line in f:
        if  not line.startswith(">"):
            seq+=line.strip()
print(seq)
protein=""
for i in range(0,len(seq),3):
    codon=seq[i:i+3]
    protein+=gen_cod.get(codon,"X")
print(protein)