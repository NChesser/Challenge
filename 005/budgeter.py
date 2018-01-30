# budget program, where I can enter in my expenses and it will store results
# perhaps I can also incorperate some graphs or something

import sqlite3
import random

# might want to change the database name, if I want this to be a budget program
EXPENSE_DATABASE = "expenses.db"
EXPENSE_TYPES = ("FOOD", "RENT", "UTILITIES", "ENTERTAINMENT", "MISC")

# Perhaps I need an income table
def create_database():
    db = sqlite3.connect(EXPENSE_DATABASE)
    cursor = db.cursor()
    cursor.execute('''DROP TABLE expenses''')
    db.commit()
    cursor.execute("CREATE TABLE expenses(uid INTEGER PRIMARY KEY, type TEXT, cost INTEGER)")
    db.commit()
    db.close()

def get_expenses(expense_type):
    db = sqlite3.connect(EXPENSE_DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT cost, type FROM expenses WHERE type=?", (expense_type,))
    
    values = [row for row in cursor]

    for row in values:
        print('{0} : {1}'.format(row[0], row[1]))

    print(expense_type + " Total: " + str(sum([row[0] for row in values])))

    db.close()

def add_expense(uid, expense_type, cost):
    db = sqlite3.connect(EXPENSE_DATABASE)
    cursor = db.cursor()

    if expense_type in EXPENSE_TYPES:
        cursor.execute("INSERT INTO expenses(uid, type, cost) \
                            VALUES(?,?,?)", (uid, expense_type, cost))
    
    db.commit()
    db.close()

#create_database()

#for i in range(100):
    #add_expense(i, random.choice(EXPENSE_TYPES), random.randrange(1000))

get_expenses("FOOD")
print()
get_expenses("RENT")
print()
get_expenses("MISC")

