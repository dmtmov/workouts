from fastapi import FastAPI
from sqlalchemy import create_engine


app = FastAPI(
    redoc_url=None,
)


engine = create_engine(
    "sqlite:///sqlite.db",
    connect_args={"check_same_thread": False},
)


from admin import UserAdmin
from sqladmin import Admin
admin = Admin(app, engine)
admin.register_model(UserAdmin)


@app.get("/users/{id}")
def get_item():
    from models import UserSchema, UserModel

    user_orm = UserModel(id=1, name='heyyyy')

    return UserSchema.from_orm(user_orm)


@app.get("/users")
def get_item_list():
    return "hey"

