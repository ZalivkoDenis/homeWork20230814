class User:
    __cls_count = 0

    def __init__(self, first_name: str, last_name: str, login: str, password: str = ''):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.password = password
        self.__id = User.__cls_count
        User.__cls_count += 1

    @property
    def id(self):
        return self.__id

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        self._first_name = value

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        self._last_name = value

    @property
    def login(self) -> str:
        return self._login

    @login.setter
    def login(self, value: str):
        self._login = value

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str):
        self._password = value

    def __str__(self):
        return (f'id={self.id}: {self.last_name} {self.first_name}:\n'
                f'\tlogin:\t\t{self.login}\n\tpassword:\t{self.password}')
