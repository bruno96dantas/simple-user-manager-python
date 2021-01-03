

users = []


def create_user(name, nick, role, access, date):
    user = {
        "name": name,
        "nick": nick,
        "role": role,
        "access": access,
        "date": date
    }
    users.append(user)
    print(users)


def get_user(name):
    # busca o usuario dentro da lista, passando o nome no parametro
    users.get(name)


def search_super_user():
    users


def delete_user(name):
    users


def get_access(type_access):
    users


def get_user_for_date(date):
    users


if __name__ == '__main__':
    name = input("Qual seu nome completo? ")
    nick = input("Qual seu primeiro nome? ")
    role = input("Qual o seu cargo? ")
    access = input("Qual o seu nível de acesso? ")
    create_user(name, nick, role, access, date=False)
