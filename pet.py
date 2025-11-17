class Pet():
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
    def shockcollar(self):
        print("you have press shock collar button.")
        print(f"your pets happiness level went down by 5")
        self.happinesslevel -= 5
    def feed(self):
        fchoice = ['bread','poop','pet treats','leftovers','fruits','vegetables']
        print(f"food choices: {fchoice}")
        food = input(f"what do you want to feed your pet?: ").lower()
        print(f"you fed your pet {food}")
        if food == 'bread':
            self.hungerlevel += 2
            print(f"your pets hunger level went up by 2")
        elif food == 'poop':
            self.hungerlevel -= 2
            self.happinesslevel -= 10
            print(f"your pets hunger level went down by 2")
            print(f"your pets happiness level went down by 10")
        elif food == 'pet treats':
            self.hungerlevel += 2
            self.happinesslevel += 10
            print(f"your pets hunger level went up by 2")
            print(f"your pets happiness level went up by 10")
        elif food == 'leftovers':
            self.hungerlevel += 1
            print(f"your pets hunger level went up by 1")
        elif food == 'fruits':
            self.hungerlevel += 2
            self.happinesslevel += 1
            print(f"your pets hunger level went up by 2")
            print(f"your pets happiness level went up by 1")
        elif food == 'vegetables':
            self.hungerlevel += 1
            print(f"your pets hunger level went up by 1")
        else:
            print(f"you fed your pet {food}")
            print(f"nothing happened because you cant feed them {food} lol")
    def walk(self):
        print("you are now walking your pet.")
        print(f"your pets happiness level went up by 2")
        self.happinesslevel += 2
    def show_rules(self):
        print("how to play the game:")
        print("type 1 to check age")
        print("type 2 to check hunger level")
        print("type 3 to check happiness")
        print("type 4 to use shock collar")
        print("type 5 to feed")
        print("type 6 to walk your pet")
        print("type 'stop' to stop game")
        print("type 'rules' to check rules again")
    def stats(self):
        print("pet stats:")
        print(f"name: {pet1.name}")
        print(f"age: {pet1.age}")
        print(f"pet type: {pet1.type}")
        print(f"achievements: {achievements}")
a = input("do you want to make and play with a virtual pet? type yes or no: ").lower()
#conditional statement to start making a character
if a == "no":
    print("goodbye")
elif a == "yes":
    petname = input("what do you want to name your pet?: ").lower()
    petage = int(input("how old is your pet in years?: "))
    pettype = input("what type of pet do you want?: ").lower()
    pet1 = Pet(petname, petage, pettype, 50, 50)
    print("confirm your pet stats:")
    print(f"name: {pet1.name}")
    print(f"age: {pet1.age}")
    print(f"pet type: {pet1.type}")
    print(f"all pets happiness levels start at {pet1.happinesslevel}%")
    print(f"all pets hunger levels start at {pet1.hungerlevel}%")
    b = input("type yes or no to confirm stats: ").lower()
    #loop to confirm pet stats so if user makes a mistake they could redo it
    while b == 'no':
        petname = input("what do you want to name your pet?: ")
        petage = int(input("how old is your pet in years?: "))
        pettype = input("what type of pet do you want?: ").lower()
        pet1 = Pet(petname, petage, pettype, 50, 50)
        print("confirm your pet stats:")
        print(f"name: {pet1.name}")
        print(f"age: {pet1.age}")
        print(f"pet type: {pet1.type}")
        print(f"all pets happiness levels start at {pet1.happinesslevel}%")
        print(f"all pets hunger levels start at {pet1.hungerlevel}%")
        b = input("type yes or no to confirm stats: ").lower()
    pet1.show_rules()
    #loop to finally start playing the game
    survive = True
    loops = 0
    achievements = []
    unlock = False
    while survive == True:
        import random
        event = random.randint(1,50)
        if event == 1:
            survive = False
            print("wow thats unlucky. a shooter has broke into your house!")
            print("you got shot and your pet died tough luck")
            pet1.stats()
        elif event == 0 or 10 or 20 or 30 or 40 or 50:
            print("wow, your pet just threw up. thats nasty")
            print("your pets hunger and happiness level just got halved!")
            pet1.hungerlevel = pet1.hungerlevel / 2
            pet1.happinesslevel = pet1.happinesslevel / 2
        game = input("what do you want to do?").lower()
        #age check
        if game == '1':
            pet1.agecheck()
        #hunger level check
        elif game == '2':
            pet1.hungerlevelcheck()
        #happiness level check
        elif game == '3':
            pet1.happinesslevelcheck()
            if pet1.happinesslevel >= 100:
                achievements.append("best pet owner oat")
        #shock collar
        elif game == '4':
            pet1.shockcollar()
        #feed
        elif game == '5':
            pet1.feed()
            if pet1.hungerlevel <= 0:
                survive = False
                print("lol your pet starved to death")
                achievements.append("starvation")
                print("ggs! ur done playing xiyangs super omega amazing beautiful cute fun pet game!!!!!!")
                pet1.stats()
            elif pet1.hungerlevel >= 100 and 'super owner' not in achievements:
                achievements.append('super owner')
        #walk
        elif game == '6':
            if pet1.type == 'fish':
                survive = False
                achievements.append("#1 stupid")
                print("you cant walk a fish stupid")
                print("your pet is dead now")
                pet1.stats()
            else:
                pet1.walk()
        #game end
        elif game == 'stop':
            survive = False
        #rules
        elif game == 'rules':
            pet1.show_rules()
        #ran out of happiness
        if pet1.happinesslevel <= 0:
            survive = False
            print("ur pets happiness is in the dumps. they have escaped.")
            achievements.append("hasan")
            pet1.stats()
        #every 5 plays pet grows 1 year old
        if survive == True:
            loops += 1
            if loops % 5 == 0:
                pet1.age += 1
                pet1.hungerlevel -= 5
    #end stats
    if game == "stop":
        print("ggs! ur done playing xiyangs super omega amazing beautiful cute fun pet game!!!!!!")
        pet1.stats()
else: 
    print("your input is invalid. please do not put numbers or any special characters")