# if 

dna = input('Enter DNA Seuqnece:')
agcgcgggtatatatatgcnccann

if 'n' in dna:
  nbases = dna.count('n')
  print("dna sequence has %d undefined bases " % nbases)
  
else:
  print("dna sequence has no undefined bases")

# Loops
## while loop: block of code to execute while condition is true
dna = input('Enter DNA Seuqnece:')
pos = dna.find('gt', 0) # position of donor splice site

while pos > -1:
  pos = dna.find('gt', pos + 1)
  print("Donor splice site condidate at position %d" % pos)

## for loop: it iterates over the items of any sequence, in the order that they appear in the sequence
motifs = ["attccgt", "agggggtttttcg", "gtagc"]
for m in motifs:
  print(m, len(m))
  
## range() function
The range() built-in function allows you to iterate over a sequence of numbers

for i in range(1,10,2):
  print(i)

protein = 'SDVIHRYKUUPARKSHGWYVCJ'






