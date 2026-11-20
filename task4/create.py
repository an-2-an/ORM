from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Column, Table
from sqlalchemy.orm import Session

import datetime


class Base(DeclarativeBase):
    pass

actor_movie = Table(
    "actor_movie",
    Base.metadata,
    Column("actor_id", ForeignKey("actors.id"), primary_key=True),
    Column("movie_id", ForeignKey("movies.id"), primary_key=True)
)


class Actor(Base):
    __tablename__ = "actors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    movies: Mapped[list["Movie"]] = relationship(
        secondary=actor_movie,
        back_populates="actors"
    )

    def __repr__(self):
        return self.name


class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150))
    year: Mapped[int]
    rating: Mapped[float] 

    actors: Mapped[list["Actor"]] = relationship(
        secondary=actor_movie,
        back_populates="movies"
    )

    def __repr__(self):
        return self.title


engine = create_engine("sqlite:///task4.db", echo=False)
session = Session(engine)


if __name__ == '__main__':
    Base.metadata.create_all(engine)

