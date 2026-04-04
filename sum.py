#finding the percentage of gc present in dna
dna="ATGCAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC"
gc_count=dna.count("G")+dna.count("C")

gc_percent=(gc_count/len(dna))*100
print("The percentage of GC in the DNA sequence is:", gc_percent)
