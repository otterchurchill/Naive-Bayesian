def getCompPrediction(Input,arrested,listcur,total):
    Input = zip(head,Input)
    guessVal = 1 #will eventually be our guess
    Nsamples = float(listcur[('Arrest',arrested)])
    probOverall = Nsamples / total
    #print probOverall
    for i,element in enumerate(Input):
        if i != 2:
            #print element, float(listcur[element])/ Nsamples 
            guessVal *= float(listcur[element])/ Nsamples 
    
    return guessVal*probOverall


#**********************************************************************
import math
import sys

clist = [list(line.rstrip().split(',')) for line in open(sys.argv[1])]
head = clist[0]
dlist = clist[1:]
total = len(dlist)
train = int(math.ceil(total * .8))
#print train
test = dlist[train:]
train = dlist[:train]
#print train
nolist = [zip(head,list) for list in train if list[2] == '0']
yeslist = [zip(head,list) for list in train if list[2] == '1']
#print yeslist

#ehlist = [zip(head,list) for list in dlist]


import itertools
from collections import Counter
yeslist = Counter(itertools.chain.from_iterable(yeslist))
nolist = Counter(itertools.chain.from_iterable(nolist))
#print yeslist
#print nolist

Input = ['0486','ALLEY','?','true','1422','26']

accurate = 0
for Input in test:
    Correct = Input[2]
    yes = getCompPrediction(Input, '1', yeslist, total)
    no = getCompPrediction(Input, '0', nolist, total)
    #print Input

    #print 'yes: ', yes, 'no', no
    if yes > no:
        #print "this instance will lead to arrest."
        if Correct == '1':
            #print "good guess"
            accurate +=1
    #if yes == no:
        #print "no prediction can be made"
    if no > yes:
        #print "this instance will not lead to arrest."
        if Correct == '0':
            #print "good guess"
            accurate += 1

print "Final Accuracy for Arrests with Naive Bayes",float(accurate)/len(test)
print "*******************************************************************"


