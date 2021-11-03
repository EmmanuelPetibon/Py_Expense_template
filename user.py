from PyInquirer import prompt
import csv


user_questions = [
    {
        "type":"input",
        "name":"username",
        "message":"New User - Username: ",
    },
]

colors = {
    "RED": "\033[91m",
    "NC": "\033[0m",
    "CYAN": "\033[96m"
}

def add_user(users, *args):
    # This function should create a new user, asking for its name
    user_infos = prompt(user_questions)

    # --- Update the users list ---
    infos_list  = [user_infos['username']]
    users.append(infos_list)

    # --- Persist new user inside a csv file ---
    with open('data/users.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        writer.writerow(infos_list)

    print(f"{colors['CYAN']}User Added !{colors['NC']}")

    return True