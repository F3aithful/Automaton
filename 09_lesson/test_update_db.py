from db_methods import CreateOnject

db = CreateOnject("postgresql://postgres:123@localhost:5432/postgres")

def test_update_user():


   test_id = 919999

# Создание пользователя и проверка его сохранения в БД
   db.create_object(test_id, "ivanivanovich@mail.ru", 1)

# Обновление почты пользователя и проверка обновления данных
   db.update_object("new_email@mail.ru", test_id)

   user = db.get_user_by_id(test_id)
   assert user is not None
   assert user["user_email"] == "new_email@mail.ru"

# Удление созданного пользователя
   db.delete_object(test_id)

# Проверяем что его больше нет
   user = db.get_user_by_id(test_id)
   assert user is None