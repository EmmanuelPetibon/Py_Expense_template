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


colors = {
    "RED": "\033[91m",
    "NC": "\033[0m",
    "CYAN": "\033[96m"
}


def new_expense(expenses, *args):
    # --- New User's Answers --- #
    infos       = prompt(expense_questions)

    # --- Verify User's Answers --- #
    if not infos['amount'].isnumeric() or infos['label'].isnumeric() or infos['spender'].isnumeric():
        print(f"{colors['RED']}Wrong Expense specified !{colors['NC']}")
        return False

    # --- Update the expenses list ---
    infos_list  = [infos['amount'], infos['label'], infos['spender']]
    expenses.append(infos_list)

    # --- Persist new expense inside a csv file ---
    with open('data/expense_report.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        writer.writerow(infos_list)
    

        print(f"{colors['CYAN']}Expense Added !{colors['NC']}")

    return True


