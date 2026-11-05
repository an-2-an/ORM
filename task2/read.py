from create import Category, session, Product
from sqlalchemy import select


if __name__ == '__main__':
    stmt = select(Product).order_by(Product.price.desc())

    for obj in session.scalars(stmt):
        print(obj, obj.price, obj.category)

    print('* ' * 20)

    stmt = select(Category).order_by(Category.name)

    for obj in session.scalars(stmt):
        print(obj, obj.products)

    print('* ' * 20)

    stmt = select(Category, Product)

    for tpl in session.execute(stmt):
        print(tpl)

    