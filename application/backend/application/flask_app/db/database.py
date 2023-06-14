import os

from dotenv import load_dotenv

from sqlalchemy import create_engine, text as sql_text
from sqlalchemy.orm import scoped_session, sessionmaker

# This is only used in local dev mode
try:
    load_dotenv("../../../../.env.local")
except FileNotFoundError:
    pass


DB_SCHEMA = "nakji"


def get_database_url(testing=False):
    database_url = "postgresql://"

    if testing:
        database_url += os.getenv("TEST_POSTGRES_USER", "test_user") + ":"
        database_url += os.getenv("TEST_POSTGRES_PASSWORD", "postgres") + "@"
        database_url += os.getenv("TEST_POSTGRES_HOST", "localhost") + ":"
        database_url += os.getenv("TEST_POSTGRES_PORT", "5432") + "/"
        database_url += os.getenv("TEST_POSTGRES_DB", "test_local_db")
    else:
        database_url += os.getenv("POSTGRES_USER", "erickim") + ":"
        database_url += os.getenv("POSTGRES_PASSWORD", "postgres") + "@"
        database_url += os.getenv("POSTGRES_HOST", "localhost") + ":"
        database_url += os.getenv("POSTGRES_PORT", "5432") + "/"
        database_url += os.getenv("POSTGRES_DB", "local_rec_db")
    
    return database_url

SQLALCHEMY_DATABASE_URL = get_database_url()
TEST_DB_URI = get_database_url(testing=True)

def get_db_loaded_session(db_uri):
    print("Creating db engine")
    print(db_uri)
    
    engine = create_engine(db_uri)

    db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return db_session


def db_session_provider(func):
    session = get_db_loaded_session(SQLALCHEMY_DATABASE_URL)

    def wrapper(*args, **kwargs):
        output = func(session, *args, **kwargs)
        session.close()
        return output
    
    return wrapper