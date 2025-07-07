# 1. Create A list of 5 of your favorite snacks
favSnacks =["Starburst","Gummies","Doritos","Kitkats","Lays chips"]
favSnacks.append("Skittles")
favSnacks.sort()
for snack in favSnacks:
    print(snack)


# 2.Create A tuple of 5 colleges you want to attend
myColleges = ("Moore house", "Howard", "USC", "Stanford","CCC")
for College in myColleges: 
    print(College)


# 3. Create A set of with 5 pieces of data on anything you want; 
numberGrade = {33, 72, 42, 21, 94}
for grade in numberGrade:
    print(grade)


# 4. Create A dictionary on a car; key must describe an attribute of the car, followed it's value
carAttribute = { "Brand": "Toyota",
                "Model": "Corrola",
                "Year": 2023,  
                "Engine": "4-cylinder",
                "WheelSize": "18in" }
carAttribute["color"] = "blue"
for attribute in carAttribute:
    print(carAttribute.get(attribute))
