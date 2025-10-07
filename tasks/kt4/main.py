class User:
    count = 0

    def __init__(self, name: str, login: str, password: str, grade: int):
        self._name = name
        self._login = login
        self._password = password
        self._grade = grade  # гарантированно int
        User.count += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        print("Невозможно изменить логин!")

    @property
    def password(self):
        return "********"

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def grade(self):
       return 'Неизвестное свойство grade'
        

    @grade.setter
    def grade(self, value):
        print("Неизвестное свойство grade")

    def show_info(self):
        print(f"Name: {self._name}, Login: {self._login}")

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self._grade == other._grade

    def __ne__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self._grade != other._grade

    def __lt__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self._grade < other._grade

    def __le__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self._grade <= other._grade

    def __gt__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self._grade > other._grade

    def __ge__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self._grade >= other._grade


class SuperUser(User):
    count = 0

    def __init__(self, name: str, login: str, password: str, grade: int, role: str):
        super().__init__(name, login, password, grade)
        self._role = role
        SuperUser.count += 1
        User.count -= 1  # корректировка, т.к. родительский __init__ уже увеличил счётчик

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    def show_info(self):
        print(f"Name: {self._name}, Login: {self._login}, Role: {self._role}")


user1 = User('Paul McCartney', 'paul', '1234', 3)
user2 = User('George Harrison', 'george', '5678', 2)
user3 = User('Richard Starkey', 'ringo', '8523', 3)
admin = SuperUser('John Lennon', 'john', '0000',5,'admin')

user1.show_info()
admin.show_info()

users = User.count
admins = SuperUser.count

print(f'Всего обычных пользователей: {users}')
print(f'Всего супер-пользователей: {admins}')

print(user1 < user2)
print(admin > user3)
print(user1 == user3)

user3.name = 'Ringo Star'
user1.password = 'Pa$$w0rd'

print(user3.name)
print(user2.password)
print(user2.login)

user2.login = 'geo'

print(user1.grade)
admin.grade = 10
