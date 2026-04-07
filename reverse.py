dna="ATGTAGAT"
comp={"A": "T", "T": "A", "G": "C", "C": "G"}
print("".join(comp[base] for base in dna)[::-1 ])

#using function
def rev_comp(dna):
    comp={"A": "T", "T": "A", "G": "C", "C": "G"}
    return "".join(comp[base] for base in dna)[::-1 ]
print(rev_comp("CCGTAAG"))

#without using join
dna="ATGTAGAT" 
comp={"A": "T", "T": "A", "G": "C", "C": "G"}
rev_comp=" "
for base in dna:
    rev_comp=comp[base]+rev_comp
print(rev_comp)
