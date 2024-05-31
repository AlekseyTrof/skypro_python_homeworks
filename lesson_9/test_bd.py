from employee_api1 import EmployeeApi
from table_bd import Table_bd
from sqlalchemy import create_engine
import requests
import sqlalchemy

base_url = "https://x-clients-be.onrender.com"
api = EmployeeApi(base_url)
db = Table_bd('postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx')

def test_add_news_empl():
    name_company = 'Testing'
    db.create(name_company)
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

    my_headers= {}
    my_headers["x-client-token"] = api.get_token()
    requests.post(base_url+'/employee', headers=my_headers, json=body1)
    assert len(db.get_empl_in_company(max_id_company)) == 1

    requests.post(base_url+'/employee', headers=my_headers, json=body2)
    all_empl = db.get_empl_in_company(max_id_company)
    db.delete_empl(max_id_company)
    db.delete_empl(max_id_company)
    db.delete_company(max_id_company)
    assert len(all_empl) == 2

def test_get_info_new_empl():
    name_company = 'Testing'
    db.create(name_company)
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

    my_headers= {}
    my_headers["x-client-token"] = api.get_token()
    requests.post(base_url+'/employee', headers=my_headers, json=body)

    get_emp = db.get_empl_in_company(max_id_company)[0]
    db.delete_empl(max_id_company)
    db.delete_company(max_id_company)
    assert len(get_emp) == 12
    assert get_emp["first_name"] == first_name
    assert get_emp["last_name"] == last_name
    assert get_emp["phone"] == phone

def test_change_info_empl():
    name_company = 'Testing'
    db.create(name_company)
    max_id_company = db.get_max_id_company()
    my_headers= {}
    my_headers["x-client-token"] = api.get_token()
    
    first_name = 'Tester1'
    last_name = 'Test1'
    phone = '692020'
    db.add_new_empl(first_name, last_name, phone, max_id_company)

    first_name2 = "Tester new"
    last_name2 = "Tester1 new"
    email2 = "alex2@mail.ru"
    phone2 = "666 333"
    body_change = {
        "id": 0,
        "firstName": first_name2,
        "lastName": last_name2,
        "companyId": max_id_company,
        "email": email2,
        "phone": phone2,
        "isActive": True
    }
    change_info_employee = requests.patch(
        base_url+'/employee/'+max_id_company, headers=my_headers, json=body_change
        )

    get_emp = db.get_empl_in_company(max_id_company)[0]
    db.delete_empl(max_id_company)
    db.delete_company(max_id_company)
    assert get_emp["first_name"] == first_name2
    assert get_emp["last_name"] == last_name2
    assert get_emp["phone"] == phone2
