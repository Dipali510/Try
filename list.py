#list formation 
dna="ATGTG"
position="ATG"
match=0
result=[]
for i in range (len(dna)-len(position)+1):
    window=dna[i:i+len(position)]
    match=sum(1 for a,b in zip(position,window)if a==b)
    result.append((i,window,match))
print (result)
