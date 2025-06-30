# Step 1: Crete a list of every Genius at your table
geniuses = ["Marshawn", "Max", "Avery", "Semaj", "Kauri", "Devon"]

# Step 2: Loop through that list and print everyone's name to the terminal
# What type of loop are we using here?
for genius in geniuses:
    print(genius)


# Step 3: Prompt the user to print the list again
answer = input("Do you want me to print the list again? Y/N")
while answer == "Y":
    for genius in geniuses:
        print(genius)
    answer = input("Do you want me to print the list again? Y/N")