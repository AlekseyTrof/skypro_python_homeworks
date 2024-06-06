from employee_api1 import EmployeeApi
from table_bd import Table_bd
import requests
import allure

base_url = "https://x-clients-be.onrender.com"
api = EmployeeApi(base_url)
db = Table_bd('postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx')

@allure.title("Получение списка активных организаций")
@allure.description("Есть возможность добавить нового сотрудника в компанию")
@allure.feature("Employee")
@allure.severity("Critical")
def test_add_news_empl() -> None:
    """
    Проверка добавления персонала 
    путем сравнения количества человек 
    после каждого добавления нового человека
    """
    with allure.step("Выбрать название компании"):
        name_company = 'Testing'
    with allure.step("Создать компанию"):
        db.create(name_company)
    with allure.step("Получить ID созданной компании"):
        max_id_company = db.get_max_id_company()
    name1 = "Tester1"
    name2 = "Tester2"
    body1 = {
        "id": 0,
        "firstName": name1,
        "lastName": "Tester11",
        "companyId": max_id_company,
        "email": "alex1@mail.ru",
        "phone": "899202030304",
        "isActive": True
    }
    body2 = {
        "id": 0,
        "firstName": name2,
        "lastName": "Tester22",
        "companyId": max_id_company,
        "email": "alex2@mail.ru",
        "phone": "6666",
        "isActive": True
    }
    with allure.step("Получить токен для авторизации API: {my_headers}"):
        my_headers = {}
        my_headers["x-client-token"] = api.get_token()

    with allure.step("Создать нового сотрудника"):
        requests.post(base_url+'/employee', headers=my_headers, json=body1)
    with allure.step("Убедиться что список сотрудников увеличился на 1"):
        assert len(db.get_empl_in_company(max_id_company)) == 1
    with allure.step("Создать нового сотрудника в компанию"):
        requests.post(base_url+'/employee', headers=my_headers, json=body2)
    with allure.step("Получить список сотрудников компании"):
        all_empl = db.get_empl_in_company(max_id_company)
    with allure.step("Убедиться что список сотрудников в компании равен тому, сколько мы добавли сотрудников"):
        assert len(all_empl) == 2
    with allure.step("Удалить сперва сотрудников в компании"):
        db.delete_empl(max_id_company)
        db.delete_empl(max_id_company)
    with allure.step("Удалить компанию"):    
        db.delete_company(max_id_company)

@allure.title("Сравнение информации о сотруднике после создания")
@allure.description("Проверка корректности данных после создания сотрудника")
@allure.feature("Employee")
@allure.severity("Major")
def test_get_info_new_empl() -> None:
    """
    Проверка корректности передаваемых значений
    о новом сотруднике в компании
    """
    with allure.step("Выбрать название компании"):
        name_company = 'Testing'
    with allure.step("Создать компанию"):
        db.create(name_company)
    with allure.step("Получить ID созданной компании"):
        max_id_company = db.get_max_id_company()
    first_name = "Tester1"
    last_name = "Tester11"
    email = "alex1@mail.ru"
    phone = "89202030304"
    body = {
        "id": 0,
        "firstName": first_name,
        "lastName": last_name,
        "companyId": max_id_company,
        "email": email,
        "phone": phone,
        "isActive": True
    }
    with allure.step("Получить токен для авторизации API: {my_headers}"):
        my_headers = {}
        my_headers["x-client-token"] = api.get_token()
    with allure.step("Создать нового сотрудника"):
        requests.post(base_url+'/employee', headers=my_headers, json=body)
    with allure.step("Получить данные из БД о новом сотруднике"):   
        get_emp = db.get_empl_in_company(max_id_company)[0]
    with allure.step("Проверить количество количество строк информации о сотруднике"):
        assert len(get_emp) == 12
    with allure.step("Сверить имя сотрудника в БД с именем при создании"):
        assert get_emp["first_name"] == first_name
    with allure.step("Сверить фамилию сотрудника в БД с именем при создании"):    
        assert get_emp["last_name"] == last_name
    with allure.step("Сверить номер сотрудника в БД с именем при создании"):    
        assert get_emp["phone"] == phone
    with allure.step("Удалить из БД сотрудника и компанию"):
        db.delete_empl(max_id_company)
        db.delete_company(max_id_company)

@allure.title("Изменение информации о сотруднике и сравнение с результатми")
@allure.description("Проверка корректности изменения данных о сотруднике")
@allure.feature("Employee")
@allure.severity("Critical")
def test_change_info_empl() -> None:
    """
    Проверка коректного изменения данных о сотруднике в компании
    """
    with allure.step("Выбрать название компании"):
        name_company = 'Testing'
    with allure.step("Создать компанию"):
        db.create(name_company)
    with allure.step("Получить ID созданной компании"):    
        max_id_company = db.get_max_id_company()
    first_name = "Tester1"
    last_name = "Tester11"
    email = "alex1@mail.ru"
    phone = "89202030304"
    body = {
        "id": 0,
        "firstName": first_name,
        "lastName": last_name,
        "companyId": max_id_company,
        "email": email,
        "phone": phone,
        "isActive": True
    }
    with allure.step("Получить токен для авторизации API: {my_headers}"):
        my_headers = {}
        my_headers["x-client-token"] = api.get_token()
    with allure.step("Создать нового сотрудника и сразу получить его ID"):
        add_id_employee = str(requests.post(
        base_url+'/employee', headers=my_headers, json=body
        ).json()["id"])

    # Обновление информации о сотруднике
    last_name2 = "Tester1 new"
    email2 = "alex2@mail.ru"
    body_change = {
        "firstName": first_name,
        "lastName": last_name2,
        "email": email2,
        "url": "string",
        "phone": "666666",
        "isActive": False
    }
    with allure.step("Изменить данные сотрудника сотрудника"):
        requests.patch(
        base_url+'/employee/'+add_id_employee, headers=my_headers, json=body_change
        )

    with allure.step("Проверка обновленной информации о сотруднике"):
        updated_employee = db.get_empl_in_company(max_id_company)[0]
    with allure.step("Проверить что фамилия изменилась"):
        assert updated_employee["last_name"] == last_name2
    with allure.step("Удалить из БД сотрудника и компанию"):
        db.delete_empl(max_id_company)
        db.delete_company(max_id_company)
