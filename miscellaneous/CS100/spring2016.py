'''
Otmane Chaibe
'''

'''
1.A
2.D
3.C
4.D
5.B
6.E
7.C
8.D
9.D
10.E
'''
#11A
def capitalL (t,width):
    t.color('red')
    t.speed(2000)
    t.down()
    t.fd(width)
    t.left(180)
    t.fd(width)
    t.right(90)
    t.fd(width * 2)
    t.right(180)
    t.fd(width * 2)
    t.left(90)
    
#11B
def Ls (t,initWidth,multiplier,reps,angle):
    for i in range (reps):
        capitalL(t,initWidth)
        t.right(angle)
        initWidth *= multiplier

import turtle
aPen = turtle.Turtle()
s = turtle.Screen()
aPen.left(60)
Ls(aPen,20,1.5,3,20)

#question 12
def initialDict(text):
    d = {}
    words = text.split()
    for i in range(len(words)):
        ch = words[i][0].lower()
        if not ch in d:
            list1 = []
            list.append(words[i])
            d[ch] = list1
        else:
            d[ch].append(words[i])
    return d
print (initialDict('The call of the Wild'))

#question 13
def lineStats(inFile, outFile):
    inputFile = open(inFile, "r")
    outputFile = open(outFile, "w")
    for line in inputFile:
        words = line.split()
        n = len(line)
        outputFile(str(len(words))+" "+str(n-1)+"\n")

    inputFile.close()
    outputFile.close()

inF = 'promisedLand.txt'
outF = 'promisedLandStats.txt'
lineStats(inF, outF)


