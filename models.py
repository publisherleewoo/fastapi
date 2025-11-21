from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from database import Base
from sqlalchemy.orm import relationship


class Question(Base):  # database.py에서 정의한 Base 상속
    __tablename__ = "question"  # 모델에 의해 관리되는 테이블의 이름

    id = Column(Integer, primary_key=True)  # Integer 숫자
    subject = Column(
        String, nullable=False
    )  # String 제한된 글자수  nullable = not null
    content = Column(Text, nullable=False)  # Text 무제한 텍스트
    create_date = Column(DateTime, nullable=False)  # DateTime 날짜


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id")) # 외래키  question테이블의 id컬럼
    question = relationship("Question", backref="answers") #역참조
