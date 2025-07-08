# 1. Create an empty dictionary
# 2. Prompt the user for the student name key --> Add the value to the dictionary
# 3. Prompt the user for the student age key
# 4. Prompt the user for the student grade key
# 5. Use a loop to Prompt the user for the student hobbies until they enter "Done", then add the list into the dictionary
# 6. Print the dictionary to the console 

student = {}

studentName = input("Enter your student's name: ")
student["Name:"] = studentName

studentAge = input("Enter your student's age: ")
student["Age:"] = studentAge

studentGrade = input("Enter your student's grade: ")
student["Grade:"] = studentGrade

hobbies = []
hobby = input("Enter your student's hobby; Type 'done' when done: ").lower()


while hobby != "done":
    hobbies.append(hobby)
    hobby = input("Enter your student's hobby; Type 'done' when done: ").lower()
    

student["Hobbies"] = hobbies

print(student)