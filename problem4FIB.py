#number months, reproductive pairs, non-repro pairs, pair/litter,

nonrepro = 1
ofage = 0
repro = 0

months = 33
pairs = 4

for month in range(1,months):
    repro += ofage
    ofage = 0
    ofage += nonrepro # Come to age
    nonrepro = repro * pairs # Give birth

total = repro + ofage + nonrepro

print total
