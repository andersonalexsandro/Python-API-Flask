from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.extentions import db


class User(db.Model):
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  name: Mapped[str] = mapped_column(String, nullable=False)
  email: Mapped[str] = mapped_column(String, unique=True, nullable=False)