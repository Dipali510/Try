from Bio.Align import substitution_matrices
matrix = substitution_matrices.load("BLOSUM62")
seq1="ATG"
seq2="AT-"
gap=-2
score =0
for a,b in zip(seq1,seq2):
   if a=="-" or b=="-":
    score += gap
   else:
    score += matrix[a,b]
print ("score after penalty of -2 for empty space-->",score)