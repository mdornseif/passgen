
import tris
import random

passlen = 10
out = ''

pos = tris.startnum * random.random()

sum = 0
for c in tris.starts.keys():
    sum += tris.starts[c]
    if sum > pos:
        print c
        break

for i in range (passlen):
    pos = tris.tribisum[c] * random.random() 
    sum = 0
    for n in tris.tris[c].keys():
        sum += tris.tris[c][n]
        if sum > pos:
            break

    (a, b) = c
    out += a
    c = (b, n)

pos = tris.endssum[a] * random.random()
sum = 0
for n in tris.ends[a].keys():
    sum += tris.ends[a][n]
    if sum > pos:
        break

out += n
          
print out
