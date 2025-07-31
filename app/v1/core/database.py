from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_file_name = "database.db"
db_url = f"sqlite///{db_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(db_url, connect_args=connect_args)


Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    from app.v1.domains.users import models as users_models
    from app.v1.domains.bookings import models as bookings_models
    Base.metadata.create_all(bind=engine)
