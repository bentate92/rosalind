sequence = "TAATCTTAAACTGTACGTGTGCTGTTCCATGAGATATAGCGAGCATCCGGGGTAGAATGGGGACCGCTGACAGCATAGGCAGAACGACGTTTAAATGTGATGCCGGGTGTACACCCTGTGTGACACAGCTTCGGGTACGTAGGCTGACGAAAGCCGGGAGAGCTTGCATGCTTGCACCTGGTTGCTTAAGGCTATTAATCAAGCAATGGCGTTTTCTACGGCCAAATAATCCCATGCGGAAGGAAAATGGACCCAGCAAGGAACCGGAACGCAAGATTCATTGGTAGACACCCTGACGGCGCCTAGCTCATCAGCCCAGCCACGTCCGAATGCGGCTTTTACTGGCTGTCTGTAGGAATCCCCCGCTGCGGGATGGCCCGCTATTGATCCTCATTCTTAAAAGATATATAGAAGCGATGTTAAAGTCTGATGCCAGGCAAGTTCCGGGCCCGCTTCATCCAATAGCTTGAAACTGAATCGGTGAGCGGGCGGCCTATTGCTTTACACTCTCCGTAATCCTAACCCCGAACAGACTGGTTTAGATAATCGGCATTACGTACGCCCTCGTCCAGTCCTTACTTTTCGGCCAATGACACCCATCGCCTCTAATCATAGAGTTGCGCCTCCTTGCCATGTAGAACAATTAGGTCTATCCTCTGGCATTATATAACCCCCGATCTCTGTTTTTTGGGCGGAGCCCGTCACAGATACCGTTGACGAGCCTTGGGCTCACCCAACCCCCTATCAGATGATTTAAGTGGCATGAGTCCACCCTCAATTCCATCCTCTCACTTACGATGTCCCTTGTGATTTGCCTCTAGCTGGAGTCAATACTGTGTTGTGAGGTGCCGGCCCCATCTGGTGTAGAAATAAAGGTTTTACCCCCGATGGGCCACGCCCGTTGTACCTGCCGTACTGCCCCAGAACACATATCAGCCCGTCGTTG"
result = ""

for base in sequence:
    if base == "T":
        result+="U"
    else:
        result+=base

print result