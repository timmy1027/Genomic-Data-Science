print("Hello World")

5 + 5

10.5 - 2*3

10**2 ## ** is used to calculate powers

17.0//3 ## floor division dicards the fractional part

17%3 ## The % operator returns the remainder after division


# Numbers can be different types
1. Interger numbers:
  type(5)

2. Real numbers
type(3.5) ## float means real number in python
12/5 ## in python2, the result is 2, not 2.4.

3. Complex numbers
type(3+2j)
(2+4j)**2

# Strings
Strings are a series of letters surrounded by quote
1. Single quoted strings
'atg'
2. Double quoted strings
"atg"

'This is a condon, isn't it?'
"This is a condon, isn't it?" ## Use double quote when single quote is inside the text
'This is a condon, isn\'t it?' ## Otherwise, use a seperator
3. String can span multiple lines with triple quotes
""""

""""
4. Escape characters
\n newline
\t tab
\\ backslash
\" Double quote

# Basic String Operators
+ concatenate strings
* copy string(replicate)
in membership:true if first string exists inside second given string
not in non-membership:true if first string does not exist in second string

'atg' + 'gtacgtccgt'
'atg'*3
'atg' in 'atggccggcgta'

# Variables
Variables are storage containers for numbers, strings, etc.
The equal sign is used to assign a value to a variable
condon = 'atg'
dna_sequence = "gtcgcctaaccgtatattttttcccgt"

condon in dna_sequence

a = 4
a
b = a
b
b = b + 3
b

# More String Operators
[x] indexing: gives the characters at position x in a string
[x:y] slicing: gives a substring between positions x and y in a string

dna_sequence[0] # letter after position 0, which is the first one.
dna_sequence[1:3]
dna_sequence[-1] 
dna_sequence[:3]
dna_sequence[2:]


# A useful string function
The built-in function len() returns the length of a string
len(dna_sequence)


dna_sequence.count('c')
# the .(dot) operator can be interpreted as: "ask object dna_sequence to do something"

dna_sequence.upper()
# change values to capital cases
dna_sequence.find('gg')
# only the first occurance of 'gg' is reported

dna_sequence.rfind('tc')
# in reverse order

# Executing Code From a File
dna_sequence = "gtcgcctaaccgtatattttttcccgt"
no_c = dna_sequence.count('c')
no_g = dna_sequence.count('g')
dna_len = len(dna_sequence)
gc_per = (no_c + no_g) * 100 / dna_len
print(gc_per)


# Reading input
dna = input("Enter a DNA sequence, please:")

dna.count('gc')

# Some Conversion Functions
int(x [,base]) converts x to an integer
float(x) converts x to a floating-point(real) number
complex(real [,imag]) creates a complex number
str(x) converts x to a string
chr(x) converts an integer to a character

chr(65)
str(65)
float(65)


mydna = 'acgt'
mydna = mydna + mydna


dna="atgctggggact"
dna[:3]
dna
dna+1+2+3
seqlen = '10bp'
seqlen = '2' + seqlen
seqlen*2
print('>HSBGPG Human bone gla gene\\transcript "BGP"\nGGCAGATTCCCCCTAGA')

a =1
b=2
c=a+b
a=b
val = 1.234567 * 10 ** 6
val
type("1")
dna
dna.find('atg', dna.find('atg')+1)
