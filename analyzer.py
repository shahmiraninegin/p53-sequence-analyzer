import matplotlib.pyplot as plt 
file=open("data/TP53.fasta",'r')

lines=file.readlines()
sequences="" 
for line in lines:
    if not line.startswith(">"):
        sequences+=line.strip()

#sequence length
length=len(sequences)
print("sequence length:",length)
#Nucleotide count
A=sequences.count('A')
C=sequences.count('C')
G=sequences.count('G')
T=sequences.count('T')
print("A:",A)
print("C:",C)
print("G:",G)
print("T:",T)
#GC Content
gc_content=((G+C)/length)*100
print("GC_content:",round(gc_content,2),"%")
#Convert DNA_like mRNA (T) to RNA(U)
mrna_sequence=sequences.replace("T","U")

start=mrna_sequence.find("AUG")
print("start codon:",start)
coding_sequence=mrna_sequence[start:]

for i in range(0,len(coding_sequence),3):
    codon=coding_sequence[i:i+3]
protein=""
codon_table={"AUG":"M","GAG":"E","CCG":"P","CAG":"Q","UUU":"F","UUC":"F","UUA":"L","UUG":"L","UCU":"S","UCC":"S","CUU":"L","CUC":"L","CUA":"L","CUG":"L","AUU":"I","AUC":"I","AUA":"I","AUG":"M","GUU":"V","GUC":"V","GUA":"V","GUG":"V","UCU":"S","UCC":"S","UCA":"S","UCG":"S","AGU":"S","AGC":"S","CCU":"P","CCC":"P","CCA":"P","CCG":"P","ACU":"T","ACC":"T","ACA":"T","ACG":"T","GCU":"A","GCC":"A","GCA":"A","GCG":"A","UAU":"Y","UAC":"Y","CAU":"H","CAC":"H","CAA":"Q","CAG":"Q","AAU":"N","AAC":"N","AAA":"K","AAG":"K","GAU":"D","GAC":"D","GAA":"E","GAG":"E","UGU":"C","UGC":"C","UGG":"W","CGU":"R","CGC":"R","CGA":"R","CGG":"R","AGA":"R","AGG":"R","GGU":"G","GGC":"G","GGA":"G","GGG":"G","UAA":"STOP","UAG":"STOP","UGA":"STOP"}
for i in range(0,len(coding_sequence),3):
    codon=coding_sequence[i:i+3]
    if len(codon)<3:
        break
    amino_acid=codon_table[codon]
    if amino_acid=="STOP":
      break
    protein+=amino_acid
print("protein sequence:",protein)
print("protein length:",len(protein),"amino acids")
print("first 20 amino acids:",protein[0:20])
print("last 20 amino acids:",protein[-20:])

print("="*50)
print("Human Gene Sequence Analyzer")
print("="*50)
print("Gene:TP53")
print("Organism:Homo sepiens")
print()
print("Sequence length:",length)
print("GC Content",round(gc_content,2),"%")
print()
print("Protein length:",len(protein))
print()
print("First 20 amino acids:",protein[0:20])
print("Last 20 amino acids:",protein[-20:])
print("="*50)
labels=["A","C","G","T"]
counts=[A,C,G,T]
plt.bar(labels,counts)
plt.title("TP53 Nucleotide Count")
plt.xlabel("Nucleotide")
plt.ylabel("Count")

plt.savefig("output/TP53_nucleotide_count.png",dpi=300)
plt.show()




