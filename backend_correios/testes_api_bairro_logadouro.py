import requests

# Replace this with the base URL of your Flask application
BASE_URL = 'http://localhost:5000'

# Function to send a GET request and print the response
def print_response(response):
    print(f"Status code: {response.status_code}")
    try:
        print("Response:")
        print(response.json())
    except Exception as e:
        print(f"Error reading response JSON: {e}")
    print("\n")

# Test creating a new Bairro
def test_create_bairro():
    data = {
        'nome_bairro': 'Test Bairro',
        'regiao': 'Test Region',
        'cep': '12345678',
        'id_cidade': 1  # Replace with the ID of the associated Cidade
    }
    response = requests.post(f"{BASE_URL}/bairro", json=data)
    print_response(response)

# Test getting all Bairros
def test_get_bairros():
    response = requests.get(f"{BASE_URL}/bairros")
    print_response(response)

# Test getting a specific Bairro by ID
def test_get_bairro_by_id(id):
    response = requests.get(f"{BASE_URL}/bairro/{id}")
    print_response(response)

# Test updating an existing Bairro by ID
def test_update_bairro(id):
    data = {
        'nome_bairro': 'Updated Bairro',
        'regiao': 'Updated Region',
        'cep': '87654321',
        'id_cidade': 2  # Replace with the new ID of the associated Cidade
    }
    response = requests.put(f"{BASE_URL}/bairro/{id}", json=data)
    print_response(response)

# Test deleting a specific Bairro by ID
def test_delete_bairro(id):
    response = requests.delete(f"{BASE_URL}/bairro/{id}")
    print_response(response)

# Test creating a new Logradouro
def test_create_logradouro():
    data = {
        'nome_rua': 'Test Street',
        'numero': 123,
        'complemento': 'Test Complement',
        'id_bairro': 1  # Replace with the ID of the associated Bairro
    }
    response = requests.post(f"{BASE_URL}/logradouro", json=data)
    print_response(response)

# Test getting all Logradouros
def test_get_logradouros():
    response = requests.get(f"{BASE_URL}/logradouros")
    print_response(response)

# Test getting a specific Logradouro by ID
def test_get_logradouro_by_id(id):
    response = requests.get(f"{BASE_URL}/logradouro/{id}")
    print_response(response)

# Test updating an existing Logradouro by ID
def test_update_logradouro(id):
    data = {
        'nome_rua': 'Updated Street',
        'numero': 456,
        'complemento': 'Updated Complement',
        'id_bairro': 2  # Replace with the new ID of the associated Bairro
    }
    response = requests.put(f"{BASE_URL}/logradouro/{id}", json=data)
    print_response(response)

# Test deleting a specific Logradouro by ID
def test_delete_logradouro(id):
    response = requests.delete(f"{BASE_URL}/logradouro/{id}")
    print_response(response)

if __name__ == '__main__':
    # Test all CRUD operations for Bairro
    test_create_bairro()

    test_get_bairros()

    test_get_bairro_by_id(1)  # Replace 1 with the ID of the Bairro you want to retrieve

    test_update_bairro(1)  # Replace 1 with the ID of the Bairro you want to update

    test_delete_bairro(1)  # Replace 1 with the ID of the Bairro you want to delete

    # Test all CRUD operations for Logradouro
    test_create_logradouro()

    test_get_logradouros()

    test_get_logradouro_by_id(1)  # Replace 1 with the ID of the Logradouro you want to retrieve

    test_update_logradouro(1)  # Replace 1 with the ID of the Logradouro you want to update

    test_delete_logradouro(1)  # Replace 1 with the ID of the Logradouro you want to delete
