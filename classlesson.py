""" class Calculator():
    def add(x,y):
        print(x + y)
        return x+y
    def add_many(list):
        print(sum(list))
        return sum(list)
    def subtract(list):
        return list
Calculator.add(15,5)
 """

""" class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self, item):
        self.inventory.append(item)
        print(f"{self.name} purchased {item} and has {self.inventory}")
Nathan = Hero("Nathan", 0, ["Pencil"])
print(Nathan.__dict__)
Nathan.buy("Xi Yang") """

""" class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # double underscore means "private"

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}") """

#activity 1
""" class Hero:
    def __init__(character, name, inventory):
        character.name = name
        character.inventory = inventory
    def buy(character, item):
        character.inventory.append(item)
superxiyang = Hero("super xiyang", ["phone"])
superxiyang.buy("gun")
print(superxiyang.inventory) """

""" class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"
    
class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)  # Call the parent class constructor
        self.student_id = student_id
    
    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"
xiyang = Student("xiyang", "xiyangh@nycstudents.net", "240300525")
print(xiyang.display_info()) """