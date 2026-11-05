from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class Base(DeclarativeBase):
    pass

class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column(nullable=True)
    products: Mapped[List["Product"]] = relationship(
        back_populates="category"
    )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} (id={self.id!r}, name={self.name!r})"

class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column(nullable=True)
    price: Mapped[float]
    min_stock: Mapped[int]
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship(back_populates="products")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} (id={self.id!r}, name={self.name!r})"

engine = create_engine("sqlite:///task2.db", echo=False)
session = Session(engine)


if __name__ == '__main__':
    Base.metadata.create_all(engine)

