# compliment = dict()
# compliment["T"] = "A"
# compliment["A"] = "T"
# compliment["C"] = "G"
# compliment["G"] = "C"

# OR

compliment = {
    "T": "A",
    "A": "T",
    "C": "G",
    "G": "C"
}

sequence="AAAACCCGGT"
result=""

for base in sequence:
    result += compliment[base]

print result[::-1]
