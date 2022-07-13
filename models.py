from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from main import engine


Base = declarative_base()


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)


Base.metadata.create_all(engine)



from pydantic import BaseModel
class UserSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

