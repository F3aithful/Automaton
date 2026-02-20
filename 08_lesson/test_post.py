import requests

base_url = "https://ru.yougile.com/api-v2/projects"
token = " TOKEN_HEAR_PLEASE "

# Xэдеры
my_headers = {
    "Authorization": token,
    "Content-Type": "application/json"
}

# Помогатор создания проектов

def create_project(title, users):
    company = {
        "title": title,
        "users": {users: "worker"}
    }
    resp = requests.post(base_url, headers=my_headers, json=company)
    return resp


def test_add_project_positive():

# Создаем проект

    title = "VladossINC"
    users = " ID_HEAR_PLEASE "
    result = create_project(title, users)
    body = result.json()
    project_id = body.get("id")

#  Получааем созданный проект
    
    get_response = requests.get(f"{base_url}/{project_id}", headers=my_headers)
    get_body = get_response.json()

# Проверяем что: статус-код создания компании, id проекта существует, название, id проекта

    assert result.status_code == 201
    assert project_id is not None
    assert get_body["title"] == title
    assert get_body["id"] == project_id

# Авточистка если нужно
    requests.delete(f"{base_url}/{project_id}", headers=my_headers)


def test_add_project_negative():

# Инициализируем неверный токен

    inv_token = "Bearer randomtoken123"
    inv_headers = {
    "Authorization": inv_token,
    "Content-Type": "application/json"
    }
    
# Создаем компанию

    sec_company = {
    "title": "Test Project",
    "users": {
        " ID_HEAR_PLEASE ": 
        "worker"}
    }
    response = requests.post(base_url, headers=inv_headers, json=sec_company)

# Проверяем, что запрос не прошёл
    assert response.status_code == 401