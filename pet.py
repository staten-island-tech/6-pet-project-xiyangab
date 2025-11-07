class pet():
    def __init__(self, name, age, type, hungerlevel, happinesslevel):
        self.name = name
        self.age = age
        self.type = type
        self.hungerlevel = hungerlevel
        self.happinesslevel = happinesslevel
    def agecheck(self):
        print(f"your pets age is {self.age}")
    def hungerlevelcheck(self):
        print(f"your pets hunger level is {self.hungerlevel}%")
    def happinesslevelcheck(self):
        print(f"your pets happiness level is {self.happinesslevel}%")


a = input("do you want to make and play with a virtual pet? type yes or no: ").lower()
#conditional statement to start making a character
if a == "no":
    print("goodbye")
elif a == "yes":
    petname = input("what do you want to name your pet?: ")
    petage = int(input("how old is your pet in years?: "))
    pettype = input("what type of pet do you want?")
    pet1 = pet(petname, petage, pettype, 50, 0)

    print("confirm your pet stats:")
    print(f"name: {pet1.name}")
    print(f"age: {pet1.age}")
    print(f"pet type: {pet1.type}")
    print(f"all pets happiness levels start at {pet1.happinesslevel}%")
    print(f"all pets hunger levels start at {pet1.hungerlevel}%")

    b = input("type yes or no to confirm stats: ").lower()
    #loop to confirm pet stats so if user makes a mistake they could redo it
    while b != "yes":
        petname = input("what do you want to name your pet?: ")
        petage = int(input("how old is your pet in years?: "))
        pet1 = pet(petname, petage, pettype, 50, 0)

        print("confirm your pet stats:")
        print(f"name: {pet1.name}")
        print(f"age: {pet1.age}")
        print(f"pet type: {pet1.type}")
        print(f"all pets happiness levels start at {pet1.happinesslevel}%")
        print(f"all pets hunger levels start at {pet1.hungerlevel}%")

        b = input("type yes or no to confirm stats: ").lower()
        
    print("how to play the game:")
    print("type 1 to check age")
    print("type 2 to check hunger level")
    print("type 3 to check happiness")

    print("type 'stop' to stop game")
    print("type 'rules' to check rules")

    #loop to finally start playing the game
    survive = True
    loops = 0
    while survive == True:
        #have to code the rest of the game
        #i should code achievements!!

        game = input("what do you want to do?").lower()

        if game == '1':
            pet1.agecheck()

        elif game == '2':
            pet1.hungerlevelcheck()

        elif game == '3':
            pet1.happinesslevelcheck()

        elif game == 'stop':
            survive = False

        else:
            print("that is invalid. type 'rules' to check rules")

        #every 5 plays pet grows 1 year old
        loops += 1
        if loops % 5 == 0:
            pet1.age += 1
    #end stats
    if game == "stop":
        print("ggs! ur done playing xiyangs super omega amazing beautiful cute fun pet game!!!!!!")
        print("pet stats:")
        print(f"name: {pet1.name}")
        print(f"age: {pet1.age}")
        print(f"pet type: {pet1.type}")

else: 
    print("your input is invalid. please do not put numbers or any special characters")