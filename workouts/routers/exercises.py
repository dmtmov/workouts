from fastapi import Depends, APIRouter
from workouts import cruds
from workouts import deps
from workouts import schemas
from workouts.database import Session


router = APIRouter(
    prefix="/exercises",
    tags=["Exercises"]
)


@router.get("/", response_model=list[schemas.Exercise])
def _(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    return cruds.get_exercise_list(db, skip=skip, limit=limit)


@router.get("/{exercise_id}", response_model=schemas.Exercise)
def _(exercise_id: int, db: Session = Depends(deps.get_db)):
    return cruds.get_exercise(db, exercise_id)


@router.patch("/{exercise_id}", response_model=schemas.Exercise)
def _(exercise_id: int, exercise: schemas.ExerciseUpdate, db: Session = Depends(deps.get_db)):
    return cruds.update_exercise(db, exercise_id, exercise)
