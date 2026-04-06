fasta ={}
with open(r"c:\Users\dipali\OneDrive\Desktop\Try\sample.fasta") as file:
    header =""
    for line in file:
        
        if line.startswith(">"):
         header = line.strip()
         fasta[header] = ""
        else:
         fasta[header] += line
print(fasta)
for  name,seq in fasta.items():
    print("sequence",name)
    print("A:",seq.count("A"))
    print("T:",seq.count("T"))
    print("G:",seq.count("G"))
    print("C:",seq.count("C"))
print ()
#r"c:\Users\dipali\OneDrive\Documents\Custom Office Templates\butter.py\sampl.fasta"
#C:\Users\dipali\OneDrive\Documents\Custom Office Templates\butter.py