dna="ATGATGTAGAT" 
motif="ATG" 
position=[]
for i in range(0,len(dna)-len(motif)+1):
    if dna[i:i+len(motif)]==motif:
     position.append(i)
print(position)
        