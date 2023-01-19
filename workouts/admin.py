from workouts.models.exercises import Exercise, Template, Workout
from workouts import schemas
from sqlalchemy import func
from sqladmin import ModelAdmin
from workouts.models.users import UserModel


class UserAdmin(ModelAdmin, model=UserModel):
    column_list = ("id", "name")


class TemplateAdmin(ModelAdmin, model=Template):
    column_list = ("title", "exercises")
    column_searchable_list = [Template.title]
    form_columns = [Template.title]


class ExerciseAdmin(ModelAdmin, model=Exercise):
    column_list = ("template", "workout", "position", "set_id", "created_at", "updated_at")
    form_columns = [
        Exercise.workout,
        Exercise.template,
        Exercise.position,
        Exercise.set_id,
        Exercise.plan_rounds,
        Exercise.plan_repeats,
        Exercise.plan_weight
    ]


class WorkoutAdmin(ModelAdmin, model=Workout):
    column_list = ("date", "tempo", "exercises")
    form_columns = [Workout.date, Workout.tempo]

    def text_formatter(model, attribute):
        return model.__getattribute__(attribute.key).name.capitalize()

    def date_formatter(model, attribute):
        return model.__getattribute__(attribute.key).strftime("%d %B %Y %A")

    column_formatters = {
        Workout.date: date_formatter,
        Workout.tempo: text_formatter,
    }
