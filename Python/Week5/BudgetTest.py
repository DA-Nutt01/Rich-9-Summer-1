import budget

outgoings = budget.BudgetManager(2000)
outgoings.AddBudget("Rent", 800)
outgoings.AddBudget("Groceries", 400)
outgoings.PrintSummary()