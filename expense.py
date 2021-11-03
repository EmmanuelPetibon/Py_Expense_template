from PyInquirer import prompt
import csv

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },

]

def new_expense(*args):
    infos = prompt(expense_questions)

    # --- Persist new expense inside a csv file ---
    with open('expense_report.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        writer.writerow([infos['amount'], infos['label'], infos['spender']])

    print("Expense Added !")
    return True


