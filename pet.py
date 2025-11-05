class pet():
    def __init__(self, name, age, happinesslevel):
        self.name = name
        self.age = age
        self.happinesslevel = happinesslevel
    def agecheck(self):
        print(f"your pets age is {self.age}")

a = input("do you want to make and play with a virtual pet? type yes or no: ").lower()
#conditional statement to start making a character
if a == "no":
    print("goodbye")
elif a == "yes":
    petname = input("what do you want to name your pet?: ")
    petage = int(input("how old is your pet in years?: "))
    pet1 = pet(petname, petage, 0)
else: 
    print("your input is invalid. please do not put numbers or any special characters")