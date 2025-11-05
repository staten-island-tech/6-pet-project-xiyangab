#parent class
class Pet:
    def __init__(self, name, age, happinesslevel):
        self.name = name
        self.age = age
        self.__happinesslevel = happinesslevel
    def play(self, amount):
        self.__happinesslevel += amount
        print(f"u just played with {self.name}. {self.name} happiness level increase by {amount}")
    def show_happinesslevel(self):
        print(f"{self.name} happiness level is {self.__happinesslevel}")
    def showage(self):
        print(f"{self.name} age is {self.age}")

#rat child class
class rat(Pet):
    def __init__(self, name, age, happinesslevel):
        super().__init__(name, age, happinesslevel)
    def alivecheck(self):
        if self.age > 5:
            alive = False
            print("ur rat dead is probably dead")
        else:
            print("rat is probably alive")
    def play(self, amount):
        self.__happinesslevel += amount
        print(f"u just played with {self.name}. {self.name} happiness level increase by {amount}")
    def show_happinesslevel(self):
        print(f"{self.name} happiness level is {self.__happinesslevel}")
    def showage(self):
        print(f"{self.name} age is {self.age}")

#dog child class
class dog(Pet):
    def __init__(self, name, age, happinesslevel):
        super().__init__(name, age, happinesslevel)
    def alivecheck(self):
        if self.age > 15:
            alive = False
            print("ur dog dead lol")
        else:
            print("dog is probably is probably dead")
    def play(self, amount):
        self.__happinesslevel += amount
        print(f"u just played with {self.name}. {self.name} happiness level increase by {amount}")
    def show_happinesslevel(self):
        print(f"{self.name} happiness level is {self.__happinesslevel}")
    def showage(self):
        print(f"{self.name} age is {self.age}")

#cat child class
class dog(Pet):
    def __init__(self, name, age, happinesslevel):
        super().__init__(name, age, happinesslevel)
    def alivecheck(self):
        if self.age > 18:
            alive = False
            print("ur dog dead lol")
        else:
            print("dog is probably is probably dead")
    def play(self, amount):
        self.__happinesslevel += amount
        print(f"u just played with {self.name}. {self.name} happiness level increase by {amount}")
    def show_happinesslevel(self):
        print(f"{self.name} happiness level is {self.__happinesslevel}")
    def showage(self):
        print(f"{self.name} age is {self.age}")