matrix={
    ('A','A'): 4,('A','C'): 0,('A','G'): 0,('A','T'): 0,
    ('C','A'): -1,('C','C'): 9,('C','G'): -3,('C','T'): -1,
    ('G','A'): 0,('G','C'): 3,('G','G'): 5,('G','T'): 2,
    ('T','A'): 0,('T','C'): -1,('T','G'): 2,('T','T'): 5

}
seq1="AGT"
seq2="AGT"
score =0
for a,b in zip(seq1,seq2):
    score += matrix[a,b]
print(score)
