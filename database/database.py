from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "mysql+pymysql://root:root123@mysql:3306/demo"
db = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(bind=db)
Base = declarative_base()