import json

class Users:

    def check_user(self, email, password):

        with open('mydb.json', 'r') as rf:
            users = json.load(rf)

            if email not in users:
                return 0
            else:
                if password == users[email][1]:
                    return 1
                else:
                    return 0

    def check_and_add_new_user(self, name, email, password):

        with open('mydb.json', 'r') as rf:
            users = json.load(rf)

            if email in users:
                return 0
            else:
                users[email] = [name, password]
                with open('mydb.json', 'w') as wf:
                    json.dump(users, wf, indent=4)
                    return 1