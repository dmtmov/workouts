from sqlalchemy.orm import Session
from datetime import date
from workouts.models import exercises as models
from workouts import schemas


def get_workout(db: Session, workout_id: int):
    return db.query(models.Workout).filter(models.Exercise.id == workout_id).first()


def get_workout_list(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Workout).offset(skip).limit(limit).all()


def create_workout(db: Session, type: schemas.Types, date: date):
    item = schemas.WorkoutCreate(tempo=type, date=date)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def get_exercise(db, exercise_id: int):
    return db.query(models.Exercise).filter(models.Exercise.id == exercise_id).first()


def get_exercise_list(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Exercise).offset(skip).limit(limit).all()


def update_exercise(db: Session, exercise_id: int, data: schemas.ExerciseUpdate):
    item = db.query(models.Exercise).filter(models.Exercise.id == exercise_id).first()

    for key, value in data.dict(exclude_unset=True).items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)
    return item
