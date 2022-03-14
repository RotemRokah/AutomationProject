import pytest
import requests
import json
import jsonpath
import numpy as np

# @pytest.fixture()
@pytest.mark.get
def test_valid_login():
    url = "https://petstore.swagger.io/v2/user/login?username=Lola&password=123"
    # data = {'email': 'eve.holt@reqres.in', 'password': 'cityslicka'}
    response = requests.get(url)
    response_json = json.loads(response.text)
    print("Test valid login:")
    print("The response is: " + str(response_json))
    print("The status is: " + str(response.status_code))
    code = jsonpath.jsonpath(response_json, 'code')  # 'placed'
    type = jsonpath.jsonpath(response_json, 'type')  # 'placed'
    assert response.status_code == 200
    assert code[0] == 200
    assert type[0] == 'unknown'


@pytest.mark.post
def test_pet_order():
    url = "https://petstore.swagger.io/v2/store/order"
    headers = {
        'Content-Type': 'application/json'
    }
    file = open("C://Users//Public//AllProjects//Siber1//MyFinalProject//create_pet_order.json", "r")
    input_file = file.read()
    request_json = json.loads(input_file)
    print("\nTest pet order:")
    print("The request is: " + str(request_json))
    response = requests.post(url, json=request_json, headers=headers)
    response_json = json.loads(response.text)
    # id = jsonpath.jsonpath(response_json, 'id')
    petId = jsonpath.jsonpath(response_json, 'petId')  # 0
    quantity = jsonpath.jsonpath(response_json, 'quantity')  # 0
    # shipDate = jsonpath.jsonpath(response_json, 'id')
    status = jsonpath.jsonpath(response_json, 'status')  # 'placed'
    complete = jsonpath.jsonpath(response_json, 'complete')  # True
    print("The response is: " + str(response_json))
    print("The status is: " + str(response.status_code))
    assert response.status_code == 200
    assert petId[0] == 0
    assert quantity[0] == 0
    assert status[0] == 'placed'
    assert complete[0] is True


@pytest.mark.post
def test_create_user():
    url = "https://petstore.swagger.io/v2/user"
    headers = {
        'Content-Type': 'application/json'
    }
    file = open("C:\\Users\\Public\\AllProjects\\Siber1\\MyFinalProject\\create_user.json", "r")
    input_file = file.read()
    request_json = json.loads(input_file)
    print("\nTest create user:")
    print("The request is: " + str(request_json))
    response = requests.post(url, json=request_json, headers=headers)
    response_json = json.loads(response.text)
    print("The response is: " + str(response_json))
    print("The status is: " + str(response.status_code))
    status = jsonpath.jsonpath(response_json, 'status')  # 'placed'
    complete = jsonpath.jsonpath(response_json, 'complete')  # True
    code = jsonpath.jsonpath(response_json, 'code')  # 'placed'
    type = jsonpath.jsonpath(response_json, 'type')  # 'placed'
    assert response.status_code == 200
    assert code[0] == 200
    assert type[0] == 'unknown'


