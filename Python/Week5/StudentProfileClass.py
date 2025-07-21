# 1. Create an empty dictionary
# 2. Prompt the user for the student name key --> Add the value to the dictionary
# 3. Prompt the user for the student age key
# 4. Prompt the user for the student grade key
# 5. Use a loop to Prompt the user for the student hobbies until they enter "Done", then add the list into the dictionary
# 6. Print the dictionary to the console 
class StudentProfile:

    def __init__(self, name, age, grade, hobbies):
        self.student = {}
        self.student["Name"] = name
        self.student["Age"] = age
        self.student["Grade"] = grade
        self.student["Hobbies"] = hobbies


    def SetName(self):
        studentName = input("Enter your student's name: ")
        self.student["Name:"] = studentName

    def SetAge(self):
        studentAge = input("Enter your student's age: ")
        self.student["Age:"] = studentAge

    def SetGrade(self):
        studentGrade = input("Enter your student's grade: ")
        self.student["Grade:"] = studentGrade

    def SetHobbies(self):
        hobbies = []
        hobby = input("Enter your student's hobby; Type 'done' when done: ").lower()

        while hobby != "done":
            hobbies.append(hobby)
            hobby = input("Enter your student's hobby; Type 'done' when done: ").lower()
        self.student["Hobbies"] = hobbies

