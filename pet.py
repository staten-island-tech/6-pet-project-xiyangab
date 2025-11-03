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

""" rat = Pet("xiyangsrat", 78, 5)
rat.play(34)
rat.show_happinesslevel()
rat.showage() """

class rat(Pet):
    def __init__(self, name, age, happinesslevel):
        super().__init__(name, age, happinesslevel)
        if self.age > 5:
            alive = False