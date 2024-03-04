import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app import db
from typing import List

class Book(db.Model):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    author_id: Mapped[int] = mapped_column(sa.ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship(
        back_populates="books"
    )

    def __str__(self):
        return f"Book ({self.name}) by {self.author}"

    def __repr__(self):
        return str(self)


