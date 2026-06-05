
filename = "C:/Users/dipali/Downloads/sequence.fasta"





from Bio import SeqIO


seq_obj=SeqIO.read(filename,"fasta")


type(seq_obj)


seq_id=seq_obj.id
print(seq_id)


description=seq_obj.description
print(description)


sequences=seq_obj.seq
print(sequences)


lent=len(sequences)
print(lent)





