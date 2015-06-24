# cat data5.txt | python problem5.py
# Pipe the contents of data5.txt into your program

import sys
data = sys.stdin.readlines()

data.join('')

print data

# Preprocess data
inputs = []
r = range(0, len(data))
print r

for i in r:
    case = {
        "label": data[i],
        "data": data[i+1]
    }
    inputs.append(case)

print inputs
