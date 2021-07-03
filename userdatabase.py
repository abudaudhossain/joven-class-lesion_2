class UserDataBase:
    def __init__(self):
        self.users  = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if user.username < self.users[i].username:
                break
            i += 1
        self.users.insert(i, user)
        # print(self.users)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name,user.email

    def remove(self, username):
        self.users.remove(self.find(username))
    
    def list_all(self): 
        return self.users




class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email


    def __repr__(self):
        return "User(username='{}', name='{}',email='{}')".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()
    

abudaud = User('abu', 'AbDaud', 'abu@ex.com ')
sumon = User('sumon', 'Sumon Mia', 'sumon@ex.com')
sumosn = User('sumosn', 'Sumons Mia', 'sumson@ex.com')
raj = User('raj', 'Rajchowdhori','raj23@gmail.com')

database = UserDataBase()
database.insert(abudaud) 
database.insert(sumon) 
database.insert(sumosn) 
database.insert(raj)


print(database.list_all())

