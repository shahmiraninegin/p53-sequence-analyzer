# Human Gene Sequence Analyzer

A python project for analyzing the human TP53 gene sequence from a FASTA file.

## Features
- Read a FASTA file
- Count A,C,G and T nucleotides
- Calculate GC content
- Convert DNA to mRNA
- Find the start codon(AUG)
- Translate mRNA into a protein sequence
- Display protein length
- Show the first and last 20 amino acids
- Generate a nucleotide count bar chart

## Technologies
- Python
- Matplotlib

## How to Run
1.Install Matplotlib
```bash pip install matplotlib```
2.Run the program
```bash python analyzer.py```

## Example Output

```text
Sequence Length: 2512 bp
GC Content: 53.38%
Protein Length: 393 amino acids
First 20 amino acids: MEEPQSDPSVEPPLSQETFS
Last 20 amino acids: GQSTSRHKKLMFKTEGPDSD
The program generates a nucleotide count bar chart in the `output` folder.

![TP53 Nucleotide Count]https://github.com/shahmiraninegin/p53-sequence-analyzer/blob/main/output/TP53_nucleotide_count.png)
```
