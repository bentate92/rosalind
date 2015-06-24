r = open('rosalind_gc.txt')
data = r.readlines()
r.close()

samples = {}
current = ""

for character in data:
	if character[0] == ">":
		current = character[1:].rstrip()
		samples[current] = ""
	else:
		samples[current] += character.rstrip()

for s_id, s in samples.iteritems():
	samples[s_id] = (float(s.count("G") + s.count("C"))/len(s))*100

(s_id, gc) = max(list(samples.iteritems()), key = lambda item:item[1])

print s_id
print gc
