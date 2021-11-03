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


# --- Function to handle the concerned people inside the csv --- #
def str_to_list(string):
    str2 = string[2:len(string) - 2]
    return str2.split("', '")

# ------------------------------------------------- #
# --- Get the persisted data from the CSV files --- #
# ------------------------------------------------- #
def get_existing_users(filename):
    res =  []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for row in reader:
            res.append(row)

    return res


def get_existing_expenses(filename):
    res =  []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for row in reader:
            res.append([row[0], row[1], row[2], str_to_list(row[3])])

    return res



def main():
    str_to_list("['SIGL', 'RDuval', 'PChojka']")
    users       = get_existing_users('data/users.csv')
    expenses    = get_existing_expenses('data/expense_report.csv')  

    ask_option(users, expenses)
    #unittest.main()

main()