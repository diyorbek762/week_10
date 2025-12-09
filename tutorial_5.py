codon_table = {
    "ATG": "Methionine",
    "GCG": "Alanine",
    "TCC": "Serine",
    "TAT": "Tyrosine",
    "CGT": "Arginine"
}

dna_sequence = "ATGCGTTATGCG"
chunks=[]
for i in range(0, len(dna_sequence), 3):
    chunk=dna_sequence[i: i+3]
    chunks.append(chunk)
result=[]
for chunk in chunks:
    if chunk in codon_table:
        result.append(codon_table[chunk])
result='-'.join(result)
print(f"Sequence: {dna_sequence}")
print(f"Proteins: {result}")

