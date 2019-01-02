class Dog:
    """ represents a dog"""
    species= 'canis familiaris'
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []
        self.friends=[]

    def teach(self, trick):
        self.tricks.append(trick)
        print(self.name + " knows " + trick)
  

    def knows(self, chkStr):
        if chkStr in self.tricks:
            print("Yes, " + self.name + " knows " + chkStr)
            return True
        else:
            print("No, " + self.name + " doesn't know " + chkStr)
            return False
    def makefriends(self, dogobj):
        if dogobj in self.friends:
            self.friends.append(dogobj)
            print(self.name, 'your new friend is ', dogobj)
        else:
            print(self.name, 'you are already a friend with ', dogobj.)

""" problem 1"""
import dog
sugar= dog.Dog('Sugar', 'border collie')
sugar.name
sugar.breed

""" problem 2"""
sugar.tricks

""" problem 3"""
sugar.teach('frisbee')

"""problem 4"""
print(sugar.knows('frisbee'))
print(sugar.knows('arithmetic'))

"""problem 5 """
print(dog.Dog.species)
print(sugar.species)


sugar.makefriends('fred')
