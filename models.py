from sqlalchemy import Column, String, Integer, Text
from database import Base

class Todo(Base):

    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    title =  Column(String(50), unique=True)
    description = Column(Text,nullable= True)

