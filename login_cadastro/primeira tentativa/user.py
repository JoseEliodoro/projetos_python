""" from tkinter.font import names


class User():
    def __init__(self, username, name, email, password, gender):
        self.username = username
        self.name = name
        self.email = email
        self.password = password
        self.gender = gender
    
    def create_json(self):
        json = {
            'name': self.name,
            'email': self.username,
            'password': self.password,
            'username': self.username,
            'gender' : self.gender
        }
        return json """
dados = list(range(100))
def f(a, b):
    
    ans = 1
    
    for _ in range(b):
        print()
        ans /= a
        
    return ans
        
print(f(2, 3))