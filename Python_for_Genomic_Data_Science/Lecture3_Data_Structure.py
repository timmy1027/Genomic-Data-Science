# Lists
A list is an ordered set of values:
gene_expression =  ['gene', 5.15e-08, 0.000138511, 7.33e-08]
type(['gene', 5.15e-08, 0.000138511, 7.33e-08])
print(gene_expression[-1])
print(gene_expression[0])

# Modifying lists
change an individual list elements:
  gene_expression[0] = 'Lif'
gene_expression  

But you cannot change an element in a string
# Slicing lists
gene_expression[-3: ]
gene_expression[1:3] = [6.09e-07]
gene_expression

# Common List Operations
gene_expression+[5.16e-08, 0.000138511]

len(gene_expression)

del gene_expression[1]
gene_expression

# Lists As Objects
gene_expression.extend([5.16e-08, 0.000138511])
gene_expression


# Lists As Stacks
stack  = ['a', 'b', 'c', 'd']
stack.append('e')
stack

elem = stack.pop()
elem

# Sorting lists
mylist = [3,31,123,1,5]
sorted(mylist)

# Tuples 

A tuple consists of a number of values separated by commas, and is another standard sequence data
type, like strings and lists

t  = 1,2,3
t
t[0:1]

# Set
A set is an unordered collection with no duplicate elements. Set objects support mathematical
operation like union, intersection, and difference
brca1 = {'DNA repair', 'zinc ion binding', 'DNA binding', 'ubiquitin-protein transferase activity','DNA repair', 'protein ubiquitinnation'}

brca1 | brca2

| union
& intersection
- difference

# Dictionaries
A dictionary is an unordered set of key and value pairs, with the requirement
that the keys are unique (within one dictionary)

TF_motif = {'SP1' : 'gggcgg','C/EBP' : 'attgcgcaat'}

TF_motif

# Accessing Values From a Dictionary
TF_motif['SP1']

# Updating a Dictionary
TF_motif['AP1'] = 'tgagtca'
TF_motif

del TF_motif['SP1']
TF_motif

TF_motif.update({'SP1' : 'gggcgg'})
TF_motif

len(TF_motif)
list(TF_motif.keys())
list(TF_motif.values())
sorted(list(TF_motif.values()))

# Quiz 3
grades = [70,80.0,90,100]
(grades[1]+grades[3])/2

dna=input("Enter DNA sequence:")



