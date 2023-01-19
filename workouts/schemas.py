from enum import IntEnum
from datetime import date
from typing import Optional

from pydantic import BaseModel
from workouts.database import Base


class UserSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class Types(IntEnum):
    easy = 0
    hard = 1


class Exercise(BaseModel):
    id: int
    position: int
    set_id: Optional[int]

    plan_rounds: Optional[int]
    plan_repeats: Optional[int]
    plan_weight: Optional[int]

    # plan_reps_for_min: int | None

    rounds: Optional[int]
    repeats: Optional[int]
    weight: Optional[int]

    # reps_for_min: int | None
    # is_compound: bool
    # compound_order: int | None

    class Config:
        orm_mode = True


class ExerciseUpdate(BaseModel):
    position: Optional[int]
    set_id: Optional[int]

    rounds: Optional[int]
    repeats: Optional[int]
    weight: Optional[int]

    class Config:
        orm_mode = True


class Workout(BaseModel):
    id: int
    tempo: int
    date: date
    exercises: list[Exercise]

    class Config:
        orm_mode = True


class WorkoutCreate(BaseModel):
    tempo: int
    date: date
    exercises_id: list[int]

    class Config:
        orm_mode = True
