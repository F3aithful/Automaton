from db_methods import CreateOnject

db = CreateOnject("postgresql://postgres:123@localhost:5432/postgres")

def test_create_user():

    test_id = 10003
    
# Получение доступа к БД и проверка подключения
    db_enter = db.get_tables()
    assert len(db_enter) > 0

# Создание пользователя и проверка его сохранения в БД
    db.create_object(test_id, "ivanivanovich@mail.ru", 1)

    user = db.get_user_by_id(test_id)
    assert user is not None
    assert user["user_email"] == "ivanivanovich@mail.ru"

# Удление созданного пользователя
    db.delete_object(test_id)

# Проверяем что его больше нет
    user = db.get_user_by_id(test_id)
    assert user is None