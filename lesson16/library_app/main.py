from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db import DBRepository
from menu import Menu


def main():
    connection_string = f'postgresql://postgres:postgres@localhost:5432/postgres'
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()
    repo = DBRepository(session=session)
    menu = Menu(repo)
    while True:
        menu.show_menu()


if __name__ == "__main__":
    main()
