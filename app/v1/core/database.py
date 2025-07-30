from sqlalchemy import create_engine

db_file_name = "database.db"
db_url = f"sqlite///{db_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(db_url, connect_args=connect_args)
