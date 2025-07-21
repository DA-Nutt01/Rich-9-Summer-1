class userInput:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def SetName(self):
        self.name = input("Hi, Im python, what's your name!")
        print("Hello," + self.name + ", it's nice to meet you!")

    def SetAge(self):
        self.age = input ("How old are you?")
        print("That's cool I'm !")

    def SetGrade(self):
        self.grade = input ("What grade are you in?")
        print("That,s cool!")

    def PrintUser(self):
        print(f"Your name is {self.name}. you are {self.age} years old. You are in {self.grade} grade.")

