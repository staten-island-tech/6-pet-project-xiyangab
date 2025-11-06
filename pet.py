class pet():
    def __init__(self, name, age, type, happinesslevel):
        self.name = name
        self.age = age
        self.type = type
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
    pettype = input("what type of pet do you want?")
    pet1 = pet(petname, petage, pettype, 0)

    print("confirm your pet stats:")
    print(f"name: {pet1.name}")
    print(f"age: {pet1.age}")
    print(f"pet type: {pet1.type}")
    print(f"all pets happiness levels start at {pet1.happinesslevel}%")

    b = input("type yes or no to confirm stats: ").lower()
    #loop to confirm pet stats so if user makes a mistake they could redo it
    while b != "yes":
        petname = input("what do you want to name your pet?: ")
        petage = int(input("how old is your pet in years?: "))
        pet1 = pet(petname, petage, 0)

        print("confirm your pet stats:")
        print(f"name: {pet1.name}")
        print(f"age: {pet1.age}")
        print(f"pet type: {pet1.type}")
        print(f"all pets happiness levels start at {pet1.happinesslevel}%")

        b = input("type yes or no to confirm stats: ").lower()
        
    print("how to play the game:")
    print("type 1 to check age")
    print("type 2 to feed")
    print("type 3 to train")

    #loop to finally start playing the game
    cont = True
    while cont != True:
        #have to code the rest of the game
        #i should code achievements!!

        cont == False
    
    #end stats
    if cont == False:
        print("ggs! ur done playing xiyangs super omega amazing beautiful cute fun pet game!!!!!!")
        print("pet stats:")
        print("confirm your pet stats:")
        print(f"name: {pet1.name}")
        print(f"age: {pet1.age}")
        print(f"pet type: {pet1.type}")

else: 
    print("your input is invalid. please do not put numbers or any special characters")