
#1
def twoWords(length,firstLetter):
    firstWord=""
    secondWord=""

    while True:
        firstWord=input("Enter a letter word of length" + str(length) + "please:   ")
        if length == len(firstWord):
            break

    while True:

        secondWord =("Enter a word beginning with" + firstLetter+ "proceed:  ")
        if secondWord[0] == firstLetter.upper() or secondWord[0] == firstLetter.lower():
           break
    return [firstWord,secondWord]

UserLen=int(input("Please enter the length: "))

UserLett=input("please enter a letter: ")

print(twoWords(UserLen,UserLett))


#2
def twoWords(length,firstLetter):
    firstWord=""
    secondWord=""

    while True:
        firstWord=input("Enter a letter word of length" + str(length) + "please:   ")
        if length == len(firstWord):
            continue

    while True:

        secondWord =("Enter a word beginning with" + firstLetter+ "proceed:  ")
        if secondWord[0] == firstLetter.upper() or secondWord[0] == firstLetter.lower():
           continue
    return [firstWord,secondWord]

UserLen=int(input("Please enter the length: "))

UserLett=input("please enter a letter: ")

print(twoWords(UserLen,UserLett))



#3
def enterNewPassword():
	
    while True:
        s = input("\n\nEnter password: ")

        if 15 < len(s) < 8 or sum(str.isdigit(c) for c in s) < 1:

            print("Password must be 8-15 chars long and contain at least one digit:")

            continue
        else:

            print("The password is valid.")

            break



#4
import random
n = random.randrange(0,50)
print("the random numbers are generated")

Userguess = False
while Userguess  == False:
    InputbyUser = int(input("Guess please: "))
    if InputbyUser==n:
        Userguess = True
        print("Congratulation!!!!")
    elif InputbyUser>50:
        print("the range is between 0 to 50, guess lower please")
    elif InputbyUser<0:
        print("the range is between 0 to 50 guess higher")
    elif InputbyUser >n:
        print("Try one more time,guess lower")
    elif InputbyUser < n:
        print("Try one more time, guess higher")

print("End of program")

