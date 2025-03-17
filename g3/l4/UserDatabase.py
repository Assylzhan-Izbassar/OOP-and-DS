from User import User

class UserDatabase:
    def __init__(self):
        self._users = set()

    @property
    def users(self):
        return self._users

    def add_user(self, user):
        self.users.add(user)

    def has_user(self, email):
        for user in self.users:
            if user.email == email:
                return True
        return False

    def print(self):
        for user in self.users:
            print(user)


def execute():
    db = UserDatabase()
    u1 = User('Alice', 'alice@example.com', '12234')
    u2 = User('Bob', 'bob@example.com', '1234udn')

    db.add_user(u1)
    db.add_user(u2)
    db.add_user(u1)  # The user is already exist

    print(db.has_user('alice@example.com')) # True
    print(db.has_user('assyl@example.com')) # False

    db.print()

if __name__ == '__main__':
    execute()
    
