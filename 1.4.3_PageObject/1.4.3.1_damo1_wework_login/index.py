from login import Login
from register import Register


class Index:
    def go_to_login(self):
        #click login
        return Login()
    def go_to_register(self):
        #click  register
        return Register()