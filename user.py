from PyInquirer import prompt
import csv


user_questions = [
    {
        "type":"input",
        "name":"username",
        "message":"New User - Username: ",
    },
]

def add_user(*args):
    # This function should create a new user, asking for its name
    user_infos = prompt(user_questions)

    # --- Persist new user inside a csv file ---
    with open('users.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        writer.writerow([user_infos['username']])

        print("User Added !")
    return True