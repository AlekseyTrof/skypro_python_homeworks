import requests
from employee_api import EmployeeApi

base_url = 'https://x-clients-be.onrender.com'

api = EmployeeApi(base_url)

def test_status_code():
    create_id = api.create_company_id("lesson", "descr")
    id_company = {
        'company': create_id
    }


    resp = requests.get(base_url+'/employee', params=id_company)

    assert resp.status_code == 200
    
def test_add_new_empl():
    create_id = api.create_company_id("lesson", "descr")
    id_company = {
        'company': create_id
    }

    body = {
        "id": 0,
        "firstName": "test",
        "lastName": "tester",
        "middleName": "tester37",
        "companyId": create_id,
        "email": "alex@mail.ru",
        "url": "string",
        "phone": "899202030304",
        "birthdate": "2024-05-29T07:39:54.200Z",
        "isActive": True
    }

    my_headers= {}
    my_headers["x-client-token"] = api.get_token()

    resp = requests.post(base_url+'/employee', headers=my_headers, json=body)

    get_empl = requests.get(base_url+'/employee', params=id_company).json
    
    assert get_empl()[0]["phone"] == "899202030304"
    assert get_empl()[0]["companyId"] == create_id
    assert get_empl()[0]["firstName"] == "test"
    assert get_empl()[0]["lastName"] == "tester"
    assert get_empl()[0]["isActive"] == True

def test_aded_news_empl():

    create_id = api.create_company_id("lesson", "descr")
    id_company = {
        'company': create_id
    }

    my_headers= {}
    my_headers["x-client-token"] = api.get_token()

    body1 = {
        "id": 0,
        "firstName": "test1",
        "lastName": "tester1",
        "middleName": "tester37",
        "companyId": create_id,
        "email": "alex1@mail.ru",
        "url": "string",
        "phone": "899202030304",
        "birthdate": "2024-05-29T07:39:54.200Z",
        "isActive": True
    }

    resp1 = requests.post(base_url+'/employee', headers=my_headers, json=body1)
    get_empl_1 = requests.get(base_url+'/employee', params=id_company).json 
    assert len(get_empl_1()) == 1

    body2 = {
        "id": 0,
        "firstName": "test2",
        "lastName": "tester2",
        "middleName": "tester37",
        "companyId": create_id,
        "email": "alex2@mail.ru",
        "url": "string",
        "phone": "899202030304",
        "birthdate": "2024-05-29T07:39:54.200Z",
        "isActive": True
    }

    resp2 = requests.post(base_url+'/employee', headers=my_headers, json=body2)
    get_empl_2 = requests.get(base_url+'/employee', params=id_company).json
    assert len(get_empl_2()) == 2

def test_get_empl():
    create_id = api.create_company_id("lesson8", "descrip")
    id_company = {
        'company': create_id
    }

    body = {
        "id": 0,
        "firstName": "test000",
        "lastName": "tester",
        "middleName": "tester37",
        "companyId": create_id,
        "email": "alex@mail.ru",
        "url": "string",
        "phone": "899202030304",
        "birthdate": "2024-05-29T07:39:54.200Z",
        "isActive": True
    }

    my_headers= {}
    my_headers["x-client-token"] = api.get_token()

    add_id_employee = str(requests.post(
        base_url+'/employee', headers=my_headers, json=body
        ).json()["id"])

    get_employee = requests.get(base_url+'/employee/'+add_id_employee).json

    assert get_employee()["phone"] == "899202030304"
    assert get_employee()["companyId"] == create_id
    assert get_employee()["firstName"] == "test000"
    assert get_employee()["lastName"] == "tester"
    assert get_employee()["isActive"] == True

def test_change_info_empl():
    create_id = api.create_company_id("lesson81", "descrip")
    id_company = {
        'company': create_id
    }

    my_headers= {}
    my_headers["x-client-token"] = api.get_token()

    body = {
        "id": 0,
        "firstName": "test000",
        "lastName": "tester",
        "middleName": "tester37",
        "companyId": create_id,
        "email": "alex@mail.ru",
        "url": "string",
        "phone": "899202030304",
        "birthdate": "2024-05-29T07:39:54.200Z",
        "isActive": True
    }

    add_id_employee = str(requests.post(
        base_url+'/employee', headers=my_headers, json=body
        ).json()["id"])

    get_employee = requests.get(base_url+'/employee/'+add_id_employee).json
    assert get_employee()["phone"] == "899202030304"
    assert get_employee()["companyId"] == create_id
    assert get_employee()["firstName"] == "test000"
    assert get_employee()["lastName"] == "tester"
    assert get_employee()["isActive"] == True

    body_change = {
        "lastName": "New name",
        "email": "alena@mail.ru",
        "url": "string",
        "phone": "666666",
        "isActive": False
    }

    change_info_employee = requests.patch(
        base_url+'/employee/'+add_id_employee, headers=my_headers, json=body_change
        )

    new_get_employee = requests.get(base_url+'/employee/'+add_id_employee)
    assert new_get_employee.status_code == 200
    assert change_info_employee.status_code == 200
    assert new_get_employee.json()["isActive"] == False
    assert new_get_employee.json()["lastName"] == "New name"



