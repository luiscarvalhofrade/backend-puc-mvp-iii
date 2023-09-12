#import dependecies
import datetime

from sqlalchemy import (
    DECIMAL, Column, DateTime, Foreignkey, Integer, String,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

class Base(object):
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False
    )

Declarativebase = declarative_base(cls=Base)

class Question(Declarativebase):
    __table__ = "questions"

    id = Column(Integer, primary_key=True, autoincrement=True)

class QuestionDescription(Declarativebase):
    __table__ = "question_description"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(
        Integer,
        Foreignkey("questions.id", name="fk_question_description_questions"),
        nullable=False
    )
    question = relationship(Question, backref="question_description")
    description = Column(String(600))
    item_1 = Column(String(600))
    item_2 = Column(String(600))
    item_3 = Column(String(600))
    item_4 = Column(String(600))
    item_5 = Column(String(600))

class QuestionDetail(Declarativebase):
    __table__ = "question_details"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(
        Integer,
        Foreignkey("questions.id", name="fk_question_details_questions"),
        nullable=False
    )
    question = relationship(Question, backref="question_details")
    answer = Column(String(600))
    subejct = Column(String(100))
    topic = Column(String(100))

