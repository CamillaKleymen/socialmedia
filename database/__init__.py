from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLACHEMY_DATABASE_URL = 'sqlite:///data.db'
SQLACHEMY_DATABASE_URL = "postgresql://postgres:muxtar15ovchar@localhost/social_media"
# login password host name of DB

engine = create_engine(SQLACHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
