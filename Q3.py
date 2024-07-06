"""
Low-Level Design (LLD)
    Problem: Design an Expense Tracking and Balance Simplification System (Splitwise-like)
    Requirements:
        CRUD Operations for Users:
        Users should be able to create, read, update, and delete their accounts.
        
        Group Management:
        Users should be able to create groups and add other users to these groups.
        
        Expense Creation:
        Users should be able to create expenses mentioning the users involved.
        Expenses can be paid by multiple people.
        
        Expense Details:
        Users should be able to add expense details in the group, including amount and description.
        
        Expense Splitting Strategies:
        The system should automatically split expenses based on predefined strategies (equal split, percentage-based split, etc.).
        
        Balance Viewing:
        Users should be able to view individual balances at both the group level and individual level.
        
        Balance Simplification:
        Users should be able to settle balances efficiently, simplifying debt among group members.
"""

## Answer 

"""
Classes and Relationships
    User
    Group
    Expense
    SplitStrategy
    Balance
"""

# User
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.groups = []
        self.expenses = []

    def create_group(self, group_name):
        group = Group(group_name, self)
        self.groups.append(group)
        return group

    def add_expense(self, group, amount, description, paid_by, split_strategy):
        expense = Expense(amount, description, paid_by, split_strategy)
        group.add_expense(expense)
        self.expenses.append(expense)

    def get_balance(self):
        # Calculate and return the user's balance across all groups
        pass

    def update_details(self, name=None, email=None):
        if name:
            self.name = name
        if email:
            self.email = email

    def delete_account(self):
        # Code to delete user account
        pass

# Group
class Group:
    def __init__(self, name, created_by):
        self.name = name
        self.created_by = created_by
        self.members = [created_by]
        self.expenses = []

    def add_member(self, user):
        if user not in self.members:
            self.members.append(user)
            user.groups.append(self)

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_balances(self):
        # Calculate and return balances for all members
        pass


# Expense
class Expense:
    def __init__(self, amount, description, paid_by, split_strategy):
        self.amount = amount
        self.description = description
        self.paid_by = paid_by  # List of User objects who paid
        self.split_strategy = split_strategy
        self.splits = self.split_strategy.split(amount, paid_by)

    def get_splits(self):
        return self.splits


class SplitStrategy:
    def split(self, amount, paid_by):
        pass

class EqualSplitStrategy(SplitStrategy):
    def split(self, amount, paid_by):
        num_people = len(paid_by)
        return {user: amount / num_people for user in paid_by}

class PercentageSplitStrategy(SplitStrategy):
    def __init__(self, percentages):
        self.percentages = percentages

    def split(self, amount, paid_by):
        return {user: amount * self.percentages[user] for user in paid_by}


class Balance:
    def __init__(self):
        self.balances = {}

    def add_balance(self, user, amount):
        if user in self.balances:
            self.balances[user] += amount
        else:
            self.balances[user] = amount

    def simplify_balances(self):
        # Code to simplify balances between users
        pass

"""
Methods Overview
    User Methods:

        create_group(group_name)
        add_expense(group, amount, description, paid_by, split_strategy)
        get_balance()
        update_details(name, email)
        delete_account()
    
    Group Methods:

        add_member(user)
        add_expense(expense)
        get_balances()
    
    Expense Methods:
        
        get_splits()
    
    SplitStrategy Methods:

        split(amount, paid_by)
    
    Balance Methods:

        add_balance(user, amount)
        simplify_balances()
"""


# Create users
user1 = User(1, "Alice", "alice@example.com")
user2 = User(2, "Bob", "bob@example.com")
user3 = User(3, "Charlie", "charlie@example.com")

print(user1)
# Create a group
group = user1.create_group("Trip to Bali")

# Add members to the group
group.add_member(user2)
group.add_member(user3)


# Create expenses
user1.add_expense(group, 300, "Hotel", [user1, user2, user3], EqualSplitStrategy())
user2.add_expense(group, 150, "Dinner", [user2], PercentageSplitStrategy({user1: 0.4, user2: 0.4, user3: 0.2}))

# Get balances
balances = group.get_balances()
print(balances)

# Simplify balances
balance_simplification = Balance()
balance_simplification.simplify_balances()

