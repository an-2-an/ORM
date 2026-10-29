from create import Category, session


if __name__ == '__main__':
    category1 = Category(name='Комп\'ютерна техніка', description="Комп'ютери та комплектуючі")
    category2 = Category(name='Периферійні пристрої', description="Пристрої для введення та виведення даних")
    category3 = Category(name='Офісні меблі', description="Меблі для робочих місць")
    session.add_all([category1, category2, category3])
    session.commit()
