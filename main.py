from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin
from workouts import admin
from workouts.database import Base, engine
from workouts.routers import workouts, exercises


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

admin_panel = Admin(app, engine)
admin_panel.add_view(admin.ExerciseAdmin)
admin_panel.add_view(admin.TemplateAdmin)
admin_panel.add_view(admin.WorkoutAdmin)

app.include_router(workouts.router)
app.include_router(exercises.router)
