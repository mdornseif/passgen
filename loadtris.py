import pprint

f = open('/usr/share/dict/words','r')

tris = {}
trinum = 0
tribisum = {}
starts = {}
startnum = 0
ends = {}
endsum = {}
endnum = 0
l = f.readline()
while l:
    # remove tailing newline
    if l[-1:] == '\n':
        l = l[:-1]

    # skip short lines
    if len(l) < 3:
        l = f.readline()
        continue
    

    c = (l[0], l[1])
    if starts.has_key(c):
        starts[c] += 1
    else:
        starts[c] = 1
    startnum += 1

    c = (l[-2], l[-1])
    if ends.has_key(c[0]):
        if ends[c[0]].has_key(c[1]):
            ends[c[0]][c[1]] += 1
        else:
            ends[c[0]][c[1]] = 1 
    else:
        ends[c[0]] = {}
        ends[c[0]][c[1]] = 1 

    if endsum.has_key(c[0]):
        endsum[c[0]] +=1
    else:
        endsum[c[0]] = 1
    
    endnum += 1
    l = l[1:]
        
    for c in map(None, l[:-2], l[1:-1], l[2:]):
        if tris.has_key(c[:2]):
            if tris[c[:2]].has_key(c[2]):
                tris[c[:2]][c[2]] += 1
            else:
                tris[c[:2]][c[2]] = 1
        else:
            tris[c[:2]] = {}
            tris[c[:2]][c[2]] = 1
        trinum += 1
        if tribisum.has_key(c[:2]):
            tribisum[c[:2]] += 1
        else:
            tribisum[c[:2]] = 1
        
    
    l = f.readline()

print "startnum =", startnum
print "endnum =", endnum
print "trinum =", trinum
print "starts = ",
pprint.pprint(starts)
print "ends = ",
pprint.pprint(ends)
print "endssum = ",
pprint.pprint(endsum)
print "tribisum =",
pprint.pprint(tribisum)
print "tris = ",
pprint.pprint(tris)

    
