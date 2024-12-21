from app import db
from sqlalchemy import Integer, String, Date, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=True)
    surname: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)


class Post(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False, unique=True)
    text = Column(String, nullable=True)
    date = Column(Date, nullable=False)

    user = relationship("User", foreign_keys="Post.user_id")
