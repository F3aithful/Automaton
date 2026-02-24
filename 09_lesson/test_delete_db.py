from db_methods import CreateOnject

db = CreateOnject("postgresql://postgres:123@localhost:5432/postgres")

def test_delete_user():

    test_id = 99991

# Создание пользователя и проверка его сохранения в БД
    db.create_object(test_id, "ivanivanovich@mail.ru", 1)

# Удаление пользователя по ID
    db.delete_object(test_id)

    user = db.get_user_by_id(test_id)
    assert user is None