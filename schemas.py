from pydantic import BaseModel


class Kinds:
    easy: int = 1
    hard: int = 2


class Exercise(BaseModel):
    sets: int | None
    repeats: int | None
    weight: int | None
    reps_for_min: int | None

    kind: Kinds
    order: int
    
    is_compound: bool
    compound_order: int | None

    day: int
    week: int
    
    plan_sets: int | None
    plan_repeats: int | None
    plan_weight: int | None
    plan_reps_for_min: int | None
