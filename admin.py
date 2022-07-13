from sqladmin import ModelAdmin
from models import UserModel


class UserAdmin(ModelAdmin, model=UserModel):
    column_list = ["id", "name"]


