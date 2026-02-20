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


def test_change_progects_positive():

# Создаем компанию для изменения и сохраняем её id

    title = "VladossINC"
    users = " ID_HEAR_PLEASE "
    result = create_project(title, users)
    body = result.json()
    project_id = body.get("id")

# Изменяем проект

    new_title = "It_Was_Bad_Decision_To_Rename_This_Project"
    payload = {"title": new_title}

    put_resp = requests.put(f"{base_url}/{project_id}", headers=my_headers, json=payload)
    assert put_resp.status_code in (200, 201)
   
# Получаем отредактированную компанию

    get_response = requests.get(f"{base_url}/{project_id}", headers=my_headers)
    get_body = get_response.json()
    assert get_body["title"] == new_title
    assert get_body["id"] == project_id

    requests.delete(f"{base_url}/{project_id}", headers=my_headers)


def test_change_progects_negative():

# Создаем компанию для изменения и сохраняем её id

    title = "VladossINC"
    users = " ID_HEAR_PLEASE "
    result = create_project(title, users)
    body = result.json()
    project_id = body.get("id")

# Вместо изменения названия оставим пустое место

    new_title = ""
    payload = {"title": new_title}

# Проверяем, что запрос не прошёл

    put_resp = requests.put(f"{base_url}/{project_id}", headers=my_headers, json=payload)
    assert put_resp.status_code == 400
   
    requests.delete(f"{base_url}/{project_id}", headers=my_headers)