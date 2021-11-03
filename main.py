from PyInquirer import prompt
from examples import custom_style_2
from expense import expense_questions,new_expense
from user import add_user
import unittest

def ask_option():
    main_option = {
        "type":"list",
        "name":"main_options",
        "message":"Expense Tracker v0.1",
        "choices": ["New Expense","Show Status","New User", "Quit"]
    }
    option = prompt(main_option)
    if (option['main_options']) == "New Expense":
        new_expense()
    if (option['main_options']) == "New User":
        add_user()
    if (option['main_options']) == "Quit":
        return
    ask_option()

def main():
    ask_option()
    #unittest.main()

main()