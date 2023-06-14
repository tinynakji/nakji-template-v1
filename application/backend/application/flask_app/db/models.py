from sqlalchemy.orm import declarative_base
from sqlalchemy import MetaData

from flask_app.db.database import DB_SCHEMA

metadata_obj = MetaData(schema=DB_SCHEMA)

BaseModel = declarative_base()