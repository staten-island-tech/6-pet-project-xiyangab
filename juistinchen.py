import random
class hero:
    def _init_(self,hunger,thirst,clean,sleep,happiness,money,ap):
        self.hunger=hunger
        self.thirst=thirst
        self.clean=clean
        self.sleep=sleep
        self.happiness=happiness
        # player money
        self.money=money
        self.ap=ap

    #check if alive
    def alive(self):
        self.hunger > 0
        self.happiness >0
        self.clean > 0
        self.thirst > 0
        self.sleep > 0
    #caps stats
    def statcap(self):
        self.hunger=max(0,min(10,self.hunger))
        self.happiness=max(0,min(100,self.happiness))
        self.clean =max(0,min(100,self.clean))
        self.thirst=max(0,min(100,self.thirst))
        self.sleep =max(0,min(100,self.sleep))
    happinessloss=random.randint(5,10)
    dirtyness=random.randint(5,10)
    thirstness=random.randint(5,10)
    sleepyness=random.randint(5,10)
    name=input("Give me a name to your pet:  ")
    
options=[
"Play:$10",
"Feed:$10",
"Hydrate:$10",
"Clean:$10",
"Work:$0",
"sleep:$10"
]

justin = hero(100,100,100,100,100,100,100)

def game():    
    while True:
        hero.statcap()
        hero.alive()
        print(options)
        print("welcome to this game")
        print(options)
        action=input(":").lower()
        print(f"Here are your stats:\nHunger:{hero.hunger}\nHappiness:{hero.clean}\nHere your clean:{justin.clean}:\nHappiness{justin.happiness}\nMoney:{justin.money}")

        for i in options:
            if "sleep" in action:
                if justin.money > justin.sleep:
                    print( "Need more money")
                else:
                    justin.sleep+=5
            if "play" in action:
                if justin.happiness  > justin.money:
                    justin.happiness+=5
                else:
                    print("need more money")
            if "hydrate" in action:
                if justin.thirst < justin.money:
                    justin.thirst+=5
                else:
                    print("need more money")
            if "clean" in action:
                if justin.clean < justin.money:
                    justin.happiness +=5
                else:
                    print("need more money")
            if "work" in action:
                justin.money+35

            if "feed" in action:
                if justin.hunger < justin.money:
                    justin.hunger+=10
                else:
                    print("need more money")

            else: 
                print("Invalid moobse")
                justin.ap-=1
                if justin.ap==0:
                    justin.ap=3
    # kauhwreg = hero(100,100,100,100,0,0,15)