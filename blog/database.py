from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Database connection URL
SQL_ALCHEMY_DATABASE = "sqlite:///./blog.db"  # Ensure the path is correct and relative to the project root
engine = create_engine(SQL_ALCHEMY_DATABASE, connect_args={"check_same_thread": False})

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
class Base(DeclarativeBase): 
    pass

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()