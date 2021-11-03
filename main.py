from PyInquirer import prompt
from examples import custom_style_2
from expense import expense_questions,new_expense
from user import add_user
import csv
import unittest

def ask_option(users, expenses):
    main_option = {
        "type":"list",
        "name":"main_options",
        "message":"Expense Tracker v0.1",
        "choices": ["New Expense","Show Status","New User", "Quit"]
    }
    option = prompt(main_option)
    if (option['main_options']) == "New Expense":
        new_expense(expenses, users)
    if (option['main_options']) == "New User":
        add_user(users)
    if (option['main_options']) == "Quit":
        return
    ask_option(users, expenses)


# ------------------------------------------------- #
# --- Get the persisted data from the CSV files --- #
# ------------------------------------------------- #
def get_existing_data(filename):
    res =  []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for row in reader:
            res.append(row)

    return res



def main():
    users       = get_existing_data('data/users.csv')
    print(users)
    expenses    = get_existing_data('data/expense_report.csv')  
    print(expenses)

    ask_option(users, expenses)
    #unittest.main()

main()