from Bio.Seq import Seq
dna=Seq("AGTAGT")
print(dna)
print (dna.complement())
print (dna.reverse_complement())
print (dna.transcribe())#DNA to RNA
print (dna.translate())#RNA TO PROTEIN

k=3#k mer and finding the protein sequence
freq={}
for i in range(len(dna)-k+1):
    kmer=dna[i:i+k]
    
    print(kmer,"-->",kmer.translate())