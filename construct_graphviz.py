#!/usr/bin/python
print "digraph {"
print "dim = 10;"
print "dimen = 10;"
#print "pack = true;"
print "rank = same;"
#print "nodesep = .1;"
print "model = subset;"
print "clusterrank = local;"
#print "splines = ortho;"
print "overlap = prism;"
animal = raw_input("")

while animal != '0':
    associated = raw_input("")
    while len(associated) > 0:
        listvar = associated.split(' ')
        number = int(listvar[5])

        #for i in range(number):
        print ("    " + animal + " -> " + listvar[4] + "[label=\"" + listvar[5] + "\"];")

        associated = raw_input("")

    junk = raw_input("")

    animal = raw_input("")

print "}"