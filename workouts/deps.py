from typing import Generator

from workouts.database import Session


def get_db() -> Generator:
    try:
        db = Session()
        yield db
    finally:
        db.close()
