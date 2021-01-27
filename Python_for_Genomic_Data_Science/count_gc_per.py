dna_sequence = "gtcgcctaaccgtatattttttcccgt"
no_c = dna_sequence.count('c')
no_g = dna_sequence.count('g')
dna_len = len(dna_sequence)
gc_per = (no_c + no_g) * 100 / dna_len
print("The DNA sequence's GC content is",gc_per, "%")
print("The DNA sequence's GC content is %5.3f %%" % gc_per)


