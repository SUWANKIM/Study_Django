class User:
    num_users = 0 #class 변수
    def __init__(self, name):
        self.name = name

        User.num_users += 1


u = User('honux')
print(User.num_users, u.name)
u2 = User('crong')
print(User.num_users, u2.name)
print(User.num_users, u.num_users, u2.num_users)

