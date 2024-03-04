from sqlalchemy.orm import Mapped, mapped_column, relationship

from app import db
from typing import List


class Author(db.Model):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    books: Mapped[List["Book"]] = relationship(
        back_populates="author", cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"Author: ({self.name})"

    def __repr__(self):
        return str(self)