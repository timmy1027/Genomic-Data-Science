# Checking if Biopython is installed
import Bio

print(Bio.__version__)

# Example
Problem. Find out from what species an unkown DNA sequence came from

# Running BLAST over the Internet
from Bio.Blast import NCBIWWW
fasta_string = open("myseq.fa").read()
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)


# The BLAST Record
from Bio.Blast import NCBIXML
blast_record = NCBIWML.read(result_handle)

# Parsing BLAST Output
len(blast_record.alignments)


E_VALUE_THRESH = 0.01
for alignment in blast_record.alignments:
  for hsp in alignment.hsps:
    if hsp.expect < E_VALUE_THRESH:
      print('****Alignment****')
      print('sequence:', alignment.title)
      print('length', alignment.length)














