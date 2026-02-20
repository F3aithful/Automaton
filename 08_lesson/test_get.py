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


def test_get_project_by_id_positive():

# Создаем проект

    title = "DrStranje"
    users = " ID_HEAR_PLEASE "
    result = create_project(title, users)
    body = result.json()
    project_id = body.get("id")

# Получаем наш только что созданный проект по id

    resp = requests.get(f"{base_url}/{project_id}", headers=my_headers)
    project_data = resp.json()
    assert resp.status_code == 200
    assert project_data["title"] == title
    assert project_data["id"] == project_id

    requests.delete(f"{base_url}/{project_id}", headers=my_headers)


def test_get_project_by_id_negative():

# Создаем проект

    title = "DrStone"
    users = " ID_HEAR_PLEASE "
    result = create_project(title, users)
    body = result.json()
    project_id = body.get("id")

# Делаем запрос по неверному id

    invalid_id = "00000000-0000-0000-0000-000000000000"

# Проверяем, что запрос не прошёл

    resp = requests.get(f"{base_url}/{invalid_id}", headers=my_headers)
    assert resp.status_code == 404

    requests.delete(f"{base_url}/{project_id}", headers=my_headers)