#Task 1

class BudgetCategory:
    def __init__(self, category, budget):
        self.__category = category
        self.__budget = budget

#Task 2
    def get_category(self):
        return self.__category
    
    def get_budget(self):
        return self.__budget
    
    def set_category(self, new_category):
        self.__category = new_category

    def set_budget(self, new_budget):
        self.__budget = new_budget if new_budget >= 0 else print("Budget must be positive")
    
    def add_expense(self, amount):
        self.__budget -= amount

    def display_category_summary(self):
        print(f"{self.__category}: ${self.__budget:.2f} remaining")

budget = BudgetCategory('Groceries', 100)

print(budget.get_category()) #output: Groceries
print(budget.get_budget()) #output: 100

budget.set_category('Gas')
budget.set_budget(60)

print(budget.get_category()) #output: Gas
print(budget.get_budget()) #output: 60

budget.add_expense(50)
budget.display_category_summary() #output: Gas: $10.00 remaining