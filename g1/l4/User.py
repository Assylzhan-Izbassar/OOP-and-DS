"""
User collecting classes
"""

class User:
    def __init__(self, name: str, email: str, password: str):
        self._name = name
        self._email = email
        self._password = password

    # getter
    def get_name(self) -> str:
        return self._name

    # setter
    def set_name(self, name):
        if name is not None and name != '':
            self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if email is not None and email != '':
            self._email = email

    def __hash__(self):
        return hash(self.email + self.get_name())

    def __eq__(self, other: 'User'):
        if isinstance(other, User):
            return (self.get_name() == other.get_name() and
                    self.email == other.email)
        return False

    def __str__(self):
        return self.get_name() + ' ' + self.email

def policy(examination):
    def process():
        print('Collecting the phones')
        examination()
        print('Giving the phones back')
    return process


@policy
def examination():
    print('Exam is going on...')


examination()

user1 = User('<NAME>', '<EMAIL>', '<PASSWORD>')
user2 = User('<NAME>', '<EMAIL>', '<PASSWORD>')
user1.email = 'a.izbasar@almau.edu.kz'

print(user1.email, user2.email)

print(user1 == user2)
print(user1.email)

users = set()
users.add(user1)
users.add(user2)

for user in users:
    print(user)