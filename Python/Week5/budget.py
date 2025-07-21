# Your task is to convert this program into a class
# 1. Define your class
# 2. Create your __init__() for your class
# 3. Ceate your instance variable
# 4. Refactor your code into a class
# 5. Create a new python file called tester.py
# 6. import your budget class into your tester file
# 7. Paste your tester code into the tester file
# 8. Create an instance of your class named budget

class BudgetManager():
    def __init__(self, amount):

        # The amount of money we have to spend
        self.funds = amount 

        # A dictionary of our items we are spending our budget on
        # The key is the name of the item; the value is the budget amount for that item
        self.budgets = {}

        # A dictionary of the expenese of each budgeted item
        # The key is the name of the item, the value is the amount spent on the item
        self.expenses = {}

    # Adds an item to the budgets dictionary
    def AddBudget(self, name, amount):
        if name in self.budgets: # if the key is already in our budgets dictionary
            raise ValueError("Budget for item already exists")
        if amount > self.funds:
            raise ValueError("No can do, you are too broke")
        self.budgets[name] = amount # Adds the budgeted item to the budgets dicitonary
        self.funds -= amount # Subtracts the amount from the funds
        self.expenses[name] = 0 # Add the budgeted item to the expenses dictionary
        return self.funds

    def Spend(self, name, amount):
        if name not in self.expenses: # if the item is not in our budget
            raise ValueError("Item not in budget")
        self.expenses[name] += amount # Add the expense to the budgeted item
        budgeted = self.budgets[name]
        spent = self.expenses[name]
        return budgeted - spent

    def PrintBudget(self):
        print("Budget           Budgeted         Spent     Remaining")
        print("------------------------------------------------")
        totalBudgeted = 0
        totalSpent = 0
        totalRemaining = 0
        for name in self.budgets:
            budgeted = self.budgets[name] # store the amount associated with that key
            spent = self.expenses[name] # store the amount spent on that given item
            remainingBudget = budgeted - spent # Calculate the remaining budget for the given item
            print(f'{name:15s}, {budgeted:10.2f}, {spent:10.2f} '
                f'{remainingBudget:10.2f}')
            totalBudgeted += budgeted
            totalSpent += spent
            totalRemaining = remainingBudget
        print(f'{"Total":15s}, {totalBudgeted:10.2f}, {totalSpent:10.2f} '
                f'{totalBudgeted - totalSpent:10.2f}')

