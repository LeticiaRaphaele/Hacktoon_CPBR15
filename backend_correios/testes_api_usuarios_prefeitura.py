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

# Test creating a new Prefeitura
def test_create_prefeitura():
    data = {
        'nome_prefeitura': 'Test Prefeitura',
        'contato': 'Test Contato',
        'endereco': 'Test Endereco'
    }
    response = requests.post(f"{BASE_URL}/prefeitura", json=data)
    print_response(response)

# Test getting all Prefeituras
def test_get_prefeituras():
    response = requests.get(f"{BASE_URL}/prefeituras")
    print_response(response)

# Test getting a specific Prefeitura by ID
def test_get_prefeitura_by_id(id):
    response = requests.get(f"{BASE_URL}/prefeitura/{id}")
    print_response(response)

# Test updating an existing Prefeitura by ID
def test_update_prefeitura(id):
    data = {
        'nome_prefeitura': 'Updated Prefeitura',
        'contato': 'Updated Contato',
        'endereco': 'Updated Endereco'
    }
    response = requests.put(f"{BASE_URL}/prefeitura/{id}", json=data)
    print_response(response)

# Test deleting a specific Prefeitura by ID
def test_delete_prefeitura(id):
    response = requests.delete(f"{BASE_URL}/prefeitura/{id}")
    print_response(response)

# Test creating a new Usuario
def test_create_usuario():
    data = {
        'nome_usuario': 'Test Usuario',
        'email': 'test@example.com',
        'telefone': '1234567890'
    }
    response = requests.post(f"{BASE_URL}/usuario", json=data)
    print_response(response)

# Test getting all Usuarios
def test_get_usuarios():
    response = requests.get(f"{BASE_URL}/usuarios")
    print_response(response)

# Test getting a specific Usuario by ID
def test_get_usuario_by_id(id):
    response = requests.get(f"{BASE_URL}/usuario/{id}")
    print_response(response)

# Test updating an existing Usuario by ID
def test_update_usuario(id):
    data = {
        'nome_usuario': 'Updated Usuario',
        'email': 'updated@example.com',
        'telefone': '9876543210'
    }
    response = requests.put(f"{BASE_URL}/usuario/{id}", json=data)
    print_response(response)

# Test deleting a specific Usuario by ID
def test_delete_usuario(id):
    response = requests.delete(f"{BASE_URL}/usuario/{id}")
    print_response(response)

if __name__ == '__main__':
    # Test all CRUD operations for Prefeitura
    test_create_prefeitura()

    test_get_prefeituras()

    test_get_prefeitura_by_id(1)  # Replace 1 with the ID of the Prefeitura you want to retrieve

    test_update_prefeitura(1)  # Replace 1 with the ID of the Prefeitura you want to update

    test_delete_prefeitura(1)  # Replace 1 with the ID of the Prefeitura you want to delete

    # Test all CRUD operations for Usuario
    test_create_usuario()

    test_get_usuarios()

    test_get_usuario_by_id(1)  # Replace 1 with the ID of the Usuario you want to retrieve

    test_update_usuario(1)  # Replace 1 with the ID of the Usuario you want to update

    test_delete_usuario(1)  # Replace 1 with the ID of the Usuario you want to delete
