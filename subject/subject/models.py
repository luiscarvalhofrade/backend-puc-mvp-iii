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

class Subject(Declarativebase):
    __table__ = "subjects"

    id = Column(Integer, primary_key=True, autoincrement=True)

class SubjectDetails(Declarativebase):
    __table__ = "question_details"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(
        Integer,
        Foreignkey("subjects.id", name="fk_subject_details_subjects"),
        nullable=False
    )
    subject = relationship(Subject, backref="subject_detail")
    name = Column(String(600))

class SubjectTopics(Declarativebase):
    __table__ = "subject_topics"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(
        Integer,
        Foreignkey("subjects.id", name="fk_subject_topics_subjects"),
        nullable=False
    )
    subject = relationship(Subject, backref="subject_topics")
    topic = Column(String(600))