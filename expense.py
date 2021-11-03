from PyInquirer import prompt
import csv

colors = {
    "RED": "\033[91m",
    "NC": "\033[0m",
    "CYAN": "\033[96m"
}

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
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender",
        "choices": ["TO CHANGE"]
    },
    {
        "type":"checkbox",
        "name":"concerned",
        "message":"New Expense - Concerned Users",
        "choices": ["TO CHANGE"]
    }
]


def new_expense(expenses, users, *args):

    # Changing a question using the users list TEMPORARY SOLUTION
    flatten_users = [item for sublist in users for item in sublist]
    expense_questions[2]['choices'] = flatten_users
    expense_questions[3]['choices'] = [ {'name': x, 'checked': False} for x in flatten_users]

    # --- New User's Answers --- #
    infos       = prompt(expense_questions)

    # --- Verify User's Answers --- #
    if not infos['amount'].isnumeric() or infos['label'].isnumeric() or infos['spender'].isnumeric():
        print(f"{colors['RED']}Wrong Expense specified !{colors['NC']}")
        return False

    # --- Update the expenses list --- #
    
    # Do the average
    avg = int(infos['amount']) / len(infos['concerned'])
    print(avg)

    infos_list  = [infos['amount'], infos['label'], infos['spender'], infos['concerned'], avg]
    expenses.append(infos_list)
    print(expenses)

    # --- Persist new expense inside a csv file ---
    with open('data/expense_report.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        writer.writerow(infos_list)
    

        print(f"{colors['CYAN']}Expense Added !{colors['NC']}")

    return True


