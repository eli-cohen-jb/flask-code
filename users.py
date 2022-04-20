

class User():
    def __init__(self, _id, user_name, password) -> None:
        self.id = _id
        self.user_name = user_name
        self.password = password


users = [
    User(1, 'user1', 'password1'),
    User(2, 'user2', 'password2')
]


def authenticate(user_name, password):
    user = next(filter(lambda u: u.user_name ==
                user_name and u.password == password, users), None)
    return user


def identity(payload):
    user_id = payload['identity']
    user = next(filter(lambda u: u.id == user_id, users), None)
    return user
