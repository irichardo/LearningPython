# import json

# with open("data.json","r") as json_file:
#   data = json.load(json_file)

# spam = 'Hello'
# print('alice' * 5)
# print('Richard' 'Bob')

# This is a commit
# This is a multiline comment

# a = 1

# print('Hello World', a * 5)
# print('What is your name')
# my_name = input()
# print('It is good to meet you, {}'.format(my_name))#This prevents the print statement from executing


# javascript // 10 == '10' --> true
# //numero == palabra --> tons por que es true
# 10 == '10' -> true

# 10 === '10' -> false

# 10 + '10' -> 1010
# integer + string -> concatena

# '10' + '10' -> 20
# valor en string + valor en string -> 20

# 10 - '10' ->  0

# print('hello' == 'Hello') # No Exist the === in Python
# print(True is True)
# print(1 is 1, 2 is not 3)

# also u can use
# print((4 < 5) and ( 5 < 6)) # is
# print((4 == 4) or (5 > 6 )) # is not

# Classic syntax can also be used in python code
# You can use '&' operator and '|' operator for logical operations, but only one operator can be used at a time.


# if name != 'Alice':
#     print (name)

# json_string = json.dumps(data, indent = 4)
# print(json_string)

# def lowerName(person):
#     return person["name"].lower()
# def test():
#  print('Hello please, introduce your name for verification, thank you! ✨')
#  name = input()
#  name = input()
#  name_list =[person["name"] for person in data if person["name"] == name]
#  register_users=['Pedro', 'Luis', 'Richard', 'Manuel', 'Jose']
#  if len(name_list) > 0 :
#    print('It is good to meet you, {}'.format(name_list[0]))
#  else:
#    print('You are not Register, Your name is {} , Please stop trying to entry at this computer.'.format(name));


# test()


################################################################

# Factory Method

# data_exist = ["Richard", "Luis", "Manuel", "Jose"]

# class User:
#   def __init__(self, name):
#     self.name = name;

#   class RegisteredUser:
#       def getInfo(self):
#           return f"It's good to meet you{self}"

#   class UnregisteredUser:
#       def sendMessage(name):
#           return "You are not registered"

#   class userFactory:
#       def create_user(self, data):
#         # name = data["name"]
#         name = data
#         exist_in_data = [name for data in data_exist]
#         print(exist_in_data)
#         return 'Hola'
#         # is_registered = data["is_registered"]
#         # if is_registered:
#         #  return RegisteredUser()
#         # else:
#         #   return unRegisteredUser()


# user_factory = User("Richard")

# print(user_factory.RegisteredUser().getInfo())

# class User :
#   def __init__(self, name):
#     self.name = name


# Python no tiene tipado fuerte.
# ¿Que es tipado fuerte?


# hola = 'hola'


# print(hola +'Adios')
# print('Como estas' * 5)

# class User:
#   def __init__(self, name):
#     self.name = name;

#     def get_user(self):
#         print(self.name)
#         return self.name

# my_user = User("Richard")
# user_name = my_user.get_name()
# print(user_name)

# my_user = User("Richard")
# print(my_user.get_user())


# user = my_user.isRegistered()
# print(user.welcome())

# def user_info(user):
#    if user.is_Registered == True:
#       return 'Welcome {user.name}'
#    else:
#       return 'User has not registered'

# new_data = [person["name"] for person in data]
# print(new_data)
# print(user_info(my_user))
# print(data)

# user1 = User("Richard", True)
# user2 = User("Ariana", False)
# user3 = User("Quiensea", False)

# user_list = [user1, user2, user3]

# makes an array of all objects that exists in the .json

# for user in user_list:  #search all objects.name iterates over all objects
#  print(user.name)

# print(user_list[0].name)

import json

# with open("data.json", "r") as json_file:
#     data = json.load(json_file)


class User:
    def __init__(self, name, registered, age , interests):
        self.name = name
        self.is_registered = registered
        self.age = age
        self.interests = interests

    @staticmethod
    def load_data():
        with open("data.json", "r") as json_file:
            data = json.load(json_file)
            return data

    class isRegistered:
        def welcome(self):
            return "Welcome User"
          
        def get_data(self, name):
          return self.name

        def change_name(self, name, new_name):
            data = User.load_data()
            for user in data:
                if user["name"] == name:
                    print(user["name"])
                    user["name"] = new_name
                    with open("data.json", "w") as json_file:
                        json.dump(data, json_file, indent=2)
                        return "Your username has been changed successfully"

    # class isNotRegistered:
    #     def advertisement(self):
    #         return "User not registered"

    #     def create_user(self, name, interests):
    #         new_user = {"name": name, "interests": interests, "isRegistered": True}
    #         print(new_user)
    #         data = User.load_data()
    #         data.append(new_user)
    #         with open("data.json", "w") as json_file:
    #             json.dump(data, json_file, indent=2)
    #             return "User created successfully"


class UserManager:
    def __init__(self, data_file="data.json"):
        self.data_file = data_file

    def load_data(self):
        with open('data.json', "r") as json_file:
            return json.load(json_file)

    def save_data(self, data):
        with open('data.json', "w") as json_file:
            json.dump(data, json_file, indent=2)
            return "Files saved successfully"

    def create_user(self, name, age , interests, isRegistered = True):
        data = self.load_data()
        new_user = {
          "name":name,
          "age":age,
          "interests":interests,
          "isRegistered":isRegistered
        }
        data.append(new_user)
        self.save_data(data)
        return 'User created successfully'


def userAction(data):
    return data.name


while True:
    with open("data.json", "r") as json_file:
        user_data = json.load(json_file)
        user_list = [
            User(person["name"], person["isRegistered"], person["interests"], person["age"])
            for person in user_data
        ]
    user_input = input("Put your name: ")
    
    if user_input == "exit":
        break
    
    for person in user_list:
        if person.name == user_input:
            print("Welcome {} you wanna doing something?".format(person.name))
            while True:
                action = input("Entry some action: ")
                if action == "exit":
                    break
                elif action == "get_name":
                    user_name = person.name
                    print(f"User's name is {user_name}")
                elif action == "change_name":
                    new_name = input("Enter your new name: ")
                    update = person.isRegistered().change_name(person.name, new_name)
                    print(update)
                elif action == "get_hobbies":
                    hobbies = person.interests
                    response = " ".join(str(element) for element in hobbies)
                    print(
                        "Ok!, take all your hobbies information"
                        + " "
                        + " ".join(map(str, hobbies))
                    )

        elif user_input == "create_user":
            while True:
                name = input("Enter your name: ")
                if name == "exit":
                    break
                hobbies = input("Please enter all your hobbies: ")
                set_hobbies = hobbies.split(",")
                age = input("Introduce your age: ")
                verification = input(
                    "¿Are you sure you want to create?, type yes or no: "
                )
                while True:
                  if verification == "yes":
                    new_user = UserManager().create_user(name, age , set_hobbies);
                    print(new_user)
                    break
                  elif verification == "no":
                    print("Repeat the process again")
                    break
                  else:
                    print("wrong option, please type yes or not")
                    break
    else:
      print("User not registered, type create_user to create a new user")
