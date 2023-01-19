from sqlalchemy import Column, Enum, Integer, SmallInteger, String, ForeignKey, Date, UniqueConstraint, DateTime
from sqlalchemy.orm import relationship
from workouts import schemas
from workouts.database import Base
from sqlalchemy.sql import func


class CreateUpdateModel(Base):
    __abstract__ = True

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Workout(CreateUpdateModel):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True)
    tempo = Column(Enum(schemas.Types), nullable=False)
    date = Column(Date, nullable=False)

    exercises = relationship("Exercise", back_populates="workout", uselist=True)

    def __str__(self):
        return self.date.strftime("%d %B %Y - %A")


class Exercise(CreateUpdateModel):
    __tablename__ = "exercises"
    __table_args__ = (UniqueConstraint('position', 'workout_id', name="unique_position_workout"),)

    id = Column(Integer, primary_key=True)
    position = Column(Integer, nullable=False, autoincrement=True)

    rounds = Column(SmallInteger, nullable=True)
    repeats = Column(SmallInteger, nullable=True)
    weight = Column(Integer, nullable=True)

    plan_rounds = Column(SmallInteger, nullable=True)
    plan_repeats = Column(SmallInteger, nullable=True)
    plan_weight = Column(Integer, nullable=True)

    set_id = Column(Integer, nullable=True)

    workout_id = Column(Integer, ForeignKey("workouts.id"), nullable=False)
    workout = relationship("Workout")

    template_id = Column(Integer, ForeignKey("templates.id"), nullable=False)
    template = relationship("Template")

    def __str__(self):
        return f"{self.id}"


class Template(CreateUpdateModel):
    __tablename__ = "templates"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    exercises = relationship("Exercise", back_populates="template")

    def __str__(self):
        return f"{self.title}"
