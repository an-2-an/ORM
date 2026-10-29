from create import Category, session
from sqlalchemy import select


if __name__ == '__main__':
    stmt = select(Category)

    for obj in session.scalars(stmt):
        print(obj)

    print('* ' * 20)

    stmt = select(Category).order_by(Category.name)

    for obj in session.scalars(stmt):
        print(obj, obj.description)

    print('* ' * 20)

    stmt = select(Category).where(Category.id > 1)

    for obj in session.scalars(stmt):
        print(obj, obj.description)