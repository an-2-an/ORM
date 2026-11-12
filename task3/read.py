from create import Category, session, Product, Operation
from sqlalchemy import select, func, desc


if __name__ == '__main__':
    stmt = select(Operation).order_by(Operation.timestamp.desc())

    for op in session.scalars(stmt):
        print(op, op.product)

    print('* ' * 20)
    print('* ' * 20)

    stmt = select(Operation, Product).select_from(Operation).join(Product).order_by(Operation.timestamp.desc())

    for tpl in session.execute(stmt):
        op, pr = tpl
        print(op, pr)

    print('* ' * 20)
    print('* ' * 20)

    stmt = select(Product, Operation).select_from(Product).join(Operation).order_by(Operation.timestamp.desc())

    for tpl in session.execute(stmt):
        pr, op = tpl
        print(op.timestamp.strftime('%Y-%m-%d'), op.quantity, pr.price, pr.name, op.quantity * pr.price)

    print('* ' * 20)
    print('* ' * 20)

    stmt = (
        select(
            Product, 
            func.count(Operation.id), 
            func.sum(Operation.quantity),
            func.sum(Operation.quantity * Product.price).label('cost'),
        )
        .select_from(Product)
        .join(Operation)
        .group_by(Product.id)
        .order_by(desc('cost'))
    )

    for tpl in session.execute(stmt):
        print(tpl)

    print('* ' * 20)
    print('* ' * 20)

    stmt = (
        select(
            Product.name, 
            func.count(Operation.id), 
            func.sum(Operation.quantity),
            func.coalesce(func.sum(Operation.quantity * Product.price), 0.0).label('cost'),
        )
        .select_from(Product)
        .join(Operation, isouter=True)
        .group_by(Product.id)
        .order_by(desc('cost'))
    )

    for tpl in session.execute(stmt):
        print(tpl)

    print('* ' * 20)
    print('* ' * 20)

    stmt = (
        select(
            Category.name, 
            func.count(Operation.id), 
            func.coalesce(func.sum(Operation.quantity), 0).label('total_quantity'),
            func.coalesce(func.sum(Operation.quantity * Product.price), 0.0).label('cost'),
        )
        .select_from(Category)
        .join(Product, isouter=True)
        .join(Operation, isouter=True)
        .group_by(Category.id)
        .order_by(desc('cost'))
    )

    for tpl in session.execute(stmt):
        print(tpl)

    print('* ' * 20)
    print('* ' * 20)

    stmt = (
        select(
            func.coalesce(func.sum(Operation.quantity), 0).label('total_quantity'),
            func.coalesce(func.sum(Operation.quantity * Product.price), 0.0).label('cost'),
        )
        .select_from(Category)
        .join(Product)
        .join(Operation)
    )

    for tpl in session.execute(stmt):
        print(tpl)

    print('* ' * 20)
    print('* ' * 20)


    