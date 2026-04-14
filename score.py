from Bio.Align import substitution_matrices
matrix = substitution_matrices.load("BLOSUM62")
seq1="AGT"
seq2="AGT"
score =0
for a,b in zip(seq1,seq2):
    score += matrix[a,b]
print("score is",score)