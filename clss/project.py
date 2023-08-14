from clss.user import User
from datetime import *


class Project:
    __cls_count = 0
    __users_sorted: bool = False

    def __init__(self, name: str, date_begin: date, date_end: date, users: list[User] = None):
        self.name = name
        self.date_begin = date_begin
        self.date_end = date_end
        if users is None:
            self.users = list[User]()
        else:
            self.users = list(users)

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.__id = cls.__cls_count
        cls.__cls_count += 1
        return instance

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.__id = self.__cls_count - 1


    @property
    def id(self):
        return self.__id

    @classmethod
    def _class_count(cls):
        return cls.__cls_count


    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def users(self) -> list[User]:
        if not self.__users_sorted:
            self._users.sort(key=lambda user: (user.last_name, user.first_name))
            self.__users_sorted = True
        return self._users

    @users.setter
    def users(self, value: list[User]):
        self._users = list(value)

    @property
    def date_begin(self) -> date:
        return self._begin_date

    @date_begin.setter
    def date_begin(self, value: date):
        self._begin_date = value

    @property
    def date_end(self) -> date:
        return self._date_end

    @date_end.setter
    def date_end(self, value: date):
        self._date_end = value

    def add_user(self, value: User):
        self._users.append(value)
        self.__users_sorted = False

    def del_user(self, value: User):
        try:
            self._users.remove(value)
        finally:
            ...

    def print_users(self):
        for _ in self.users:
            print(_)

    def __str__(self) -> str:
        res: str = f'{"*"*40}\nid={self.id}\nProject name:\t{self.name}\n'
        res += f'Start project:\t{self.date_begin}\n'
        res += f'End project:\t{self.date_end}\n'
        res += ' Users '.center(40,'-') + '\n'
        for user in self.users:
            for line in str(user).split('\n'):
                res += f'\t{line}\n'
        return res
