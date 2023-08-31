from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student

if __name__ == '__main__':
    engine = create_engine('sqlite:///migrations_test.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Debugging code
    import ipdb; ipdb.set_trace()
