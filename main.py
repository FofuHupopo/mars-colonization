from urls import app
from data import db_session
from data.users import User


def addСaptain():
    session = db_session.create_session()

    captain = User(
        surname="Scott", name="Ridley", age=21,
        position="captain", speciality="research engineer",
        address="module_1", email="scott_chief@mars.org",
        hashed_password="cap",
    )

    captain.set_password(captain.hashed_password)
    session.add(captain)
    
    user1 = User(
        surname="Williams", name="Robin", age=63,
        position="senior actor", speciality="actor",
        address="module_4", email="robin_williams@mars.org",
        hashed_password="IamActor",
    )

    user1.set_password(user1.hashed_password)
    session.add(user1)
    
    user2 = User(
        surname="Einstein", name="Albert", age=144,
        position="cook", speciality="physicist",
        address="module_2", email="AlbertEinstein@mars.org",
        hashed_password="physics",
    )

    user2.set_password(user2.hashed_password)
    session.add(user2)
    
    user3 = User(
        surname="Galilei", name="Galilei", age=459,
        position="builder", speciality="mechanic",
        address="module_3", email="Galileo_Galilei@mars.org",
        hashed_password="Galilei123",
    )

    user3.set_password(user3.hashed_password)
    session.add(user3)
    
    session.commit()
    session.close()


def main():
    db_session.global_init("db/mars_colonization.db")
    
    addСaptain()
    
    app.run()


if __name__ == "__main__":
    main()
