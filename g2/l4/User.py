class UserG3:
    cnt = 0
    def __init__(self, name, email, password):
        self._id = UserG3.cnt
        self._name = name
        self._email = email
        self.__password = password
        UserG3.cnt += 1

    def get_name(self):
        return self._name

    def set_name(self, name):
        if name is not None and name != '':
            self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value is not None and value != ' ' and value != '':
            self._email = value


    def __hash__(self):
        return hash(self.get_name())


    def __eq__(self, other):
        if other is None or not isinstance(other, UserG3):
            return False
        return self.get_name() == other.get_name()


    def __str__(self) -> str:
        return self.get_name()



user1 = UserG3('<Assylzhan>', '<EMAIL>', '<PASSWORD>')
user2 = UserG3('<Assylzhan>', '<EMAIL>', '<PASSWORD>')
# print(user1.name)

print(user1.get_name())

user1.email = 'a.izbasar@email.com'
print(user1.email)

print(user1 == None)


users = set()
users.add(user1)
users.add(user2)

for user in users:
    print(user)





def policy(exam):
    def content():
        print('Сдаем телефоны')
        exam()
        print('Получаем телефоны')
    return content

@policy
def take_exam():
    print('Идет экзамен')

take_exam()








