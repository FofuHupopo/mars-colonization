from data.db_session import create_session, global_init
from data.users import User
from data.jobs import Jobs


def main():
    global_init(input())

    session = create_session()
    users = session.query(User).filter(
        User.address == 'module_1',
        User.speciality.notlike('%engineer%'),
        User.position.notlike("%engineer%")
    )

    for user in users:
        print(user.id)


if __name__ == '__main__':
    main()
