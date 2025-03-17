class User:
    cnt = 0
    def __init__(self, username, email, password):
        self.id = self.cnt
        self._username = username
        self._email = email
        self.__password = password

        self.cnt += 1

    @property
    def name(self):
        return self._username

    @name.setter
    def name(self, username):
        if (username is not None) and (username != ''):
            self._username = username

    @property
    def email(self):
        return self._email

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, User):
            return self.name == other.name
        return False


    def __str__(self):
        return f'User {self.name}'


# u1 = User("user1", "email1", "123") # создали профиль
# u2 = User("user1", "email1", "2123")
#
# print(u1.id)
# print(u2.id)
#
# users = set()
# users.add(u1)
# users.add(u2)
#
# print('Users:')
#
# for u in users:
#     print(u)
#
# # u3
# # u1.name = "no name"
# # u1.set_name('')
# # u1.name = 'name other'
#
#
#
#
# print(u1.name)
# # print(u2.name)
#
#
# # compare
# print(f'Сравнение {u1} с {u2} =',u1 == u2)