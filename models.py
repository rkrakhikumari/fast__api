from sqlalchemy import Column, String, Integer, Text
from database import Base

class Todo(Base):

    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    title =  Column(String(50), unique=True)
    description = Column(Text,nullable= True)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(130), unique=True, nullable= False)
    password = Column(String(180), nullable=False)


