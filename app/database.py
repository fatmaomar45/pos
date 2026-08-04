from pathlib import Path
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Determine a sensible default DB for local testing.
# The repository contains a school.db at the project root; compute its path
# relative to this file so the app runs regardless of current working dir.
BASE_DIR = Path(__file__).resolve().parents[2]
default_sqlite = f"sqlite:///{BASE_DIR / 'school.db'}"

# Allow overriding via environment variable for production/CI
DATABASE_URL = os.getenv("DATABASE_URL", default_sqlite)

# Create engine with SQLite-specific connect_args when needed
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, echo=False, future=True)
else:
    engine = create_engine(DATABASE_URL, echo=False, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
