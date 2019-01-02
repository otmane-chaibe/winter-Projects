'''
Otmane Chaibe
CS100 section 006
HW 05 February 10,2018
'''

""" 1a """

def hasFinalLetter(strList, letters):
    listToReturn = []

    for elements in strList:
        for letter in letters:
            if elements.endswith(letter) or elements.endswith(letter):
                listToReturn.append(elements)

    return listToReturn	      

""" 1b """

"test case 1"

strList = ["Hello PeoplE ", "ham", "Hungry"]
letters = "yE"
print(hasFinalLetter(strList, letters))

"test case 2"

strList = ["Hello", "hotel", "How"]
letters = "yE"
print(hasFinalLetter(strList, letters))

"test case 3"

strList = ["WorlD", "libra", "Bye"]
letters = "aI"
print(hasFinalLetter(strList, letters))


""" 2a """

def isDivisible(maxInt, twoInts):
    listToReturn = []
    counter = 0
    for number in range(1,maxInt):
        if number % twoInts[0] == 0 and number % twoInts[1] == 0:
            listToReturn.append(number)

    return listToReturn


""" 2b """

'''
Solution 2b
'''
"test case 1"
twoInts = (3,5)
maxInt = 36
print(isDivisible(maxInt, twoInts))

" test case 2"
twoInts = (1,2)
maxInt = 0
print(isDivisible(maxInt, twoInts))

"test case 3"
twoInts = (2,4)
maxInt = 36
print(isDivisible(maxInt, twoInts))
