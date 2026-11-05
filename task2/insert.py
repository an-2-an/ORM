from create import Category, session, Product


if __name__ == '__main__':
    category1 = Category(name='Комп\'ютерна техніка', description="Комп'ютери та комплектуючі")
    category2 = Category(name='Периферійні пристрої', description="Пристрої для введення та виведення даних")
    category3 = Category(name='Офісні меблі', description="Меблі для робочих місць")
    session.add_all([category1, category2, category3])
    product11 = Product(name="Ноутбук Lenovo IdeaPad", price=220000.0, min_stock=3, category=category1)
    product12 = Product(name="Монітор Samsung 24", price=52000.0, min_stock=4, category=category1)
    product21 = Product(name="Миша Logitech M185", price=5500.0, min_stock=5, category=category2)
    product22 = Product(name="Клавіатура Logitech K120", price=4500.0, min_stock=5, category=category2)
    product31 = Product(name="Офісне крісло", price=35000.0, min_stock=2, category=category3)
    product32 = Product(name="Стіл письмовий", price=42000.0, min_stock=1, category=category3)
    products = [product11, product12, product21, product22, product31, product32]
    session.add_all(products)
    session.commit()

