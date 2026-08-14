class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("A new user is being created...")

    def change_username(self, new_username):
        self.username = new_username

    def follow(self, user):
        self.following += 1
        user.followers += 1
        print(f"Now you are following \"{user.username}\"")

user_1 = User("001", "Cristiano romaldo")
print(user_1.id)
print(user_1.username)

user_1.change_username("Cristiano ronaldo")
print(user_1.username)
print(user_1.followers)

user_2 = User("002", "Frank zinatra")
user_2.follow(user_1)

print(user_1.followers)


