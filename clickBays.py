def getCompPrediction(Input,click,listcur,total):
    Input = zip(head,Input)
    guessVal = 1 #will eventually be our guess
    
    Nsamples = float(listcur[('click',click)])
    probOverall = Nsamples / total
    #print probOverall
    for i,element in enumerate(Input):
        if i != 0:
            #print element, float(listcur[element])/ Nsamples 
            guessVal *= float(listcur[element])/ Nsamples 
            #print "Guessupdate",element,guessVal
    
    return guessVal*probOverall


#**********************************************************************
import math
import sys
clist= []
fin = open(sys.argv[1])
head = fin.readline().rstrip().split(',')

for x,line in enumerate(fin):
    line = list(line.rstrip().split(','))
    line[1] = int(line[1]) % 100
    #print line[1]

    clist.append(line)
    if(x == 10000000):
        break
    
#print clist[:3]
dlist = clist
total = len(clist)
train = int(math.ceil(total * .8))
#print train
test = clist[train:]
train = clist[:train]
nolist = [zip(head,list) for list in train if list[0] == '0']
yeslist = [zip(head,list) for list in train if list[0] == '1']
#print yeslist[('click', 'true')]

#ehlist = [zip(head,list) for list in clist]


import itertools
from collections import Counter
yeslist = Counter(itertools.chain.from_iterable(yeslist))
nolist = Counter(itertools.chain.from_iterable(nolist))
#print yeslist
#print nolist


accurate = 0
for Input in test:
    Correct = Input[0]
    yes = getCompPrediction(Input, '1', yeslist, total)
    no = getCompPrediction(Input, '0', nolist, total)
    #print Input

    #print 'yes: ', yes, 'no', no
    if yes > no:
        #print "this instance will lead to click."
        if Correct == '1':
            #print "good guess"
            accurate +=1
    #if yes == no:
        #print "no prediction can be made"
    if no > yes:
        #print "this instance will not lead to click."
        if Correct == '0':
            #print "good guess"
            accurate += 1

print "Final Accuracy of NB for Click",float(accurate)/len(test)
print "***************************************************"


