from data.db_session import global_init, create_session
from data.users import User
from data.jobs import Jobs


def main():
    global_init(input())

    session = create_session()
    users = session.query(User).filter(User.address=="module_1")

    for user in users:
        print(user)


if __name__ == '__main__':
    main()
