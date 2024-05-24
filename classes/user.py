

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    

    def describe_user(self):
        print(f'Olá {self.first_name} {self.last_name}')
    
    def set_tentativa_login_attempts(self):
        print('Tentativa de login:' + str(self.login_attempts))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
    

user1 = User('Israel', 'Machado')

user1.describe_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.set_tentativa_login_attempts()
user1.reset_login_attempts()
user1.set_tentativa_login_attempts()

