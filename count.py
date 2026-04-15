query="ATG"
seq=["AATG","AATGATGATG "]
for base in seq:
    count=0
    for i in range(len(base)-len(query)+1):
        if base[i:i+len(query)]==query:
            count+=1
print("count of query in sequence-->",count)