class User:
    first_name = "Alex"
    last_name = "Trofimov"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def writ_fname(self):
        print(self.first_name)
    
    def writ_lname(self):
        print(self.last_name)

    def writ_fullname(self):
        print(self.first_name, self.last_name)

# Ниже проверка для кода
        
# new_user = User("Aleksey", "Trof")
# new_user.writ_fname()
# new_user.writ_lname()
# new_user.writ_fullname()