from itertools import product, takewhile
import sys

#read DNA seq from stdin
sequence = sys.stdin.readline()
print sequence

bases = "UCAG"
codons = ("".join(trio) for trio in product(bases, repeat = 3))
acids = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
amino = dict(zip(codons, acids))

protein = ""

for codon in zip(sequence[0::3], sequence[1::3], sequence[2::3]):
	#print op
	#print code
	codon = "".join(list(codon))
	#print codon
	if amino[codon] == "*":
		break
	else:
		protein += amino[codon]

print protein

#in terminal: cat ~/Downloads/'inputfilename'.txt | python problem8_take2.py