import requests

# Replace this with the base URL of your Flask application
BASE_URL = 'http://localhost:5000'

# Function to send a GET request and print the response
def print_response(response):
    print(f"Status code: {response.status_code}")
    print("Response:")
    print(response.json())
    print("\n")

# Test creating a new Estado
def test_create_estado():
    data = {
        'nome_estado': 'Test State',
        'sigla_estado': 'TS'
    }
    response = requests.post(f"{BASE_URL}/estado", json=data)
    print_response(response)

# Test getting all Estados
def test_get_estados():
    response = requests.get(f"{BASE_URL}/estados")
    print_response(response)

# Test getting a specific Estado by ID
def test_get_estado_by_id(id):
    response = requests.get(f"{BASE_URL}/estado/{id}")
    print_response(response)

# Test updating an existing Estado by ID
def test_update_estado(id):
    data = {
        'nome_estado': 'Updated State',
        'sigla_estado': 'US'
    }
    response = requests.put(f"{BASE_URL}/estado/{id}", json=data)
    print_response(response)

# Test deleting a specific Estado by ID
def test_delete_estado(id):
    response = requests.delete(f"{BASE_URL}/estado/{id}")
    print_response(response)

if __name__ == '__main__':
    # Test all CRUD operations for Estado
    test_create_estado()

    test_get_estados()

    test_get_estado_by_id(1)  # Replace 1 with the ID of the Estado you want to retrieve

    test_update_estado(1)  # Replace 1 with the ID of the Estado you want to update

    test_delete_estado(1)  # Replace 1 with the ID of the Estado you want to delete
