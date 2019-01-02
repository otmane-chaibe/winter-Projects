#problem 1

def initialLetterCount(wordList):
    dict = {}                               
    for word in wordList:                   
        firstLetter = word[0]                
        if firstLetter not in dict:         
            dict[firstLetter] = 1             
        else:                                
            dict[firstLetter] = dict[firstLetter] + 1                 
    
    return dict                                          

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton))



#problem2
def initialLetters(wordList):

    mydictionary={}

    for i in wordList:

         if  i[0] not in mydictionary:

            mydictionary[i[0]]=[i]

         elif i not in mydictionary[i[0]]:

              mydictionary[i[0]].append(i)

    return mydictionary

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say', 'with']

print(initialLetters(horton))


#problem3
def shareALetter(wordList):
    mydictionary = {}
    for word in wordList:
        if word not in mydictionary:
            mydictionary[word] = []
    for i in mydictionary.keys():
        for word in wordList:
            checkmatch = False
            for n in i:
                if n in word:
                    checkmatch=True
                    break
            if checkmatch:
                mydictionary[i].append(word)
    return mydictionary

print(shareALetter(horton))
{'I': ['I'], 'say': ['say', 'what', 'mean', 'and'], 'what': ['say', 'what', 'mean',
'and'], 'mean': ['say', 'what', 'mean', 'and'], 'and': ['say', 'what', 'mean', 'and']}
