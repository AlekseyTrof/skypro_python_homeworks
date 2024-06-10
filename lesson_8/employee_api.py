import requests

class EmployeeApi:
    """
        Функции для работы с API
    """
    def __init__(self, url):
        self.url = url

    def get_token(self, user = 'raphael', password = 'cool-but-crude'):
        user_pass = {
            'username' : user,
            'password' : password
        }

        auth = requests.post(self.url+'/auth/login', json=user_pass)
        return auth.json()["userToken"]

    def create_company_id(self, name, description=''):
        company = {
            "name": name,
            "description": description
        }

        my_headers= {}
        my_headers["x-client-token"] = self.get_token()

        resp = requests.post(self.url+'/company', json=company, headers=my_headers)
        return resp.json()["id"]

    def id_new_empl(self):
        base_url = 'https://x-clients-be.onrender.com'
        create_id = self.create_company_id("lesson", "descr")
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
        my_headers["x-client-token"] = self.get_token()

        resp = requests.post(base_url+'/employee', headers=my_headers, json=body)
        return resp.json()["id"]
