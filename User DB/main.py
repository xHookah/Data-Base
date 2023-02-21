import json, hashlib

class Register:
    def __init__(self, email: str, username: str, password: str):
        self.email = email
        self.username = username
        self.password = password

    def upload(self):
        with open("database/users.json", "r") as readJson:
            r: dict = json.load(readJson)
        hash_email = hashlib.sha256(self.email.encode()).hexdigest()
        r[hash_email] = {}
        r[hash_email]['username'] = self.username
        r[hash_email]['password'] = hashlib.sha256(self.password.encode()).hexdigest() 

        with open("database/users.json", "w") as saveJson:
            saveJson.write(json.dumps(r, indent=6))

class checker:
    def __init__(self, email: str, username: str, password: str):
        self.email = email
        self.username = username
        self.password = password

    def validate(self):
        with open("database/users.json", "r") as readJson:
            r: dict = json.load(readJson)

        hash_email = hashlib.sha256(self.email.encode()).hexdigest()

        if hash_email not in r:
            if len(self.username) < 20:
                try:
                    Register(self.email, self.username, self.password).upload()
                except Exception as error:
                    print(error)
            else:
                print("Length of the username exceeds 20 chars.")
        else:
            print("Sorry but this email is already in use.")

if __name__ == "__main__":
    email = input("Email: ")
    username = input("Username: ")
    password = input("Password: ")

    checker(email, username, password).validate()
