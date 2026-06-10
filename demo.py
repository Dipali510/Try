<<<<<<< HEAD
import pandas as pd
import matplotlib.pyplot as plt
filename="C:\\Users\\dipali\\OneDrive\\Documents\\demo.csv"
data=pd.read_csv(filename)
rdata=[data['Marks']>90]
print(rdata)

=======

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





>>>>>>> 226ba13e0a95651b07468c6a537557e8bc088479
