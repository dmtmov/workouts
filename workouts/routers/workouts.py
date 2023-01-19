from fastapi import Depends, APIRouter
from workouts import cruds
from workouts import deps
from workouts import schemas
from workouts.database import Session


router = APIRouter(
    prefix="/workouts",
    tags=["Workouts"]
)

@router.get("/", response_model=list[schemas.Workout])
def _(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    return cruds.get_workout_list(db, skip=skip, limit=limit)


@router.get("/{exercise_id}", response_model=schemas.Workout)
def _(workout_id: int, db: Session = Depends(deps.get_db)):
    return cruds.get_workout(db, workout_id)
