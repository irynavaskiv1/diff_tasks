def custom_pass(user_pass):
    return user_pass


class User:
    user_name = 3

    def password(self):
        print("User::password function")


# get attribute with name
x = getattr(User, "user_name")
print("getattr(User, 'user_name')", x)  # 3
y = getattr(User, "password")
print("getattr(User, 'password')", y)  # <function User.password at 0x7fde7e5045e0>

# add to class another method which not in class
setattr(User, "custom_pass", custom_pass)
u2 = User
z = u2.custom_pass(10)
print("u2.custom_pass(10)", z)  # 10

u3 = User
u3.new_attr1 = "value1"
# u3.__dict__['new_attr2'] = 'value'  # TypeError: 'mappingproxy' object does not support item assignment
