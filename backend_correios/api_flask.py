from flask import Flask, request, jsonify
import os
import sqlite3
import random
import string
from flask_cors import CORS

app = Flask(__name__)

CORS(app)  # Add CORS support to the entire app

# Function to get the database connection
def get_db_connection():
    db_path = os.path.join('db', 'base.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

# Function to generate a random string for testing purposes
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# Route to create a new Estado
@app.route('/estado', methods=['POST'])
def create_estado():
    data = request.get_json()
    nome_estado = data['nome_estado']
    sigla_estado = data['sigla_estado']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Estado (NomeEstado, SiglaEstado) VALUES (?, ?)', (nome_estado, sigla_estado))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Estado created successfully'}), 201

# Route to get all Estados
@app.route('/estados', methods=['GET'])
def get_estados():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Estado')
    estados = cursor.fetchall()
    conn.close()

    return jsonify([dict(estado) for estado in estados])

# Route to get a specific Estado by ID
@app.route('/estado/<int:id>', methods=['GET'])
def get_estado_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Estado WHERE ID_Estado = ?', (id,))
    estado = cursor.fetchone()
    conn.close()

    if estado is None:
        return jsonify({'message': 'Estado not found'}), 404

    return jsonify(dict(estado))

# Route to update an existing Estado by ID
@app.route('/estado/<int:id>', methods=['PUT'])
def update_estado(id):
    data = request.get_json()
    nome_estado = data['nome_estado']
    sigla_estado = data['sigla_estado']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE Estado SET NomeEstado = ?, SiglaEstado = ? WHERE ID_Estado = ?', (nome_estado, sigla_estado, id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Estado updated successfully'})

# Route to delete a specific Estado by ID
@app.route('/estado/<int:id>', methods=['DELETE'])
def delete_estado(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Estado WHERE ID_Estado = ?', (id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Estado deleted successfully'})

# Similarly, you can create routes for Cidade, Bairro, Logradouro, and Prefeitura for CRUD operations.

# Route to create a new Cidade
@app.route('/cidade', methods=['POST'])
def create_cidade():
    data = request.get_json()
    nome_cidade = data['nome_cidade']
    codigo_municipio = data['codigo_municipio']
    id_estado = data['id_estado']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Cidade (NomeCidade, CodigoMunicipio, ID_Estado) VALUES (?, ?, ?)', (nome_cidade, codigo_municipio, id_estado))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Cidade created successfully'}), 201

# Route to get all Cidades
@app.route('/cidades', methods=['GET'])
def get_cidades():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Cidade')
    cidades = cursor.fetchall()
    conn.close()

    return jsonify([dict(cidade) for cidade in cidades])

# Route to get a specific Cidade by ID
@app.route('/cidade/<int:id>', methods=['GET'])
def get_cidade_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Cidade WHERE ID_Cidade = ?', (id,))
    cidade = cursor.fetchone()
    conn.close()

    if cidade is None:
        return jsonify({'message': 'Cidade not found'}), 404

    return jsonify(dict(cidade))

# Route to update an existing Cidade by ID
@app.route('/cidade/<int:id>', methods=['PUT'])
def update_cidade(id):
    data = request.get_json()
    nome_cidade = data['nome_cidade']
    codigo_municipio = data['codigo_municipio']
    id_estado = data['id_estado']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE Cidade SET NomeCidade = ?, CodigoMunicipio = ?, ID_Estado = ? WHERE ID_Cidade = ?', (nome_cidade, codigo_municipio, id_estado, id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Cidade updated successfully'})

# Route to delete a specific Cidade by ID
@app.route('/cidade/<int:id>', methods=['DELETE'])
def delete_cidade(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Cidade WHERE ID_Cidade = ?', (id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Cidade deleted successfully'})









# Route to create a new Bairro
@app.route('/bairro', methods=['POST'])
def create_bairro():
    data = request.get_json()
    nome_bairro = data['nome_bairro']
    regiao = data['regiao']
    cep = data['cep']
    id_cidade = data['id_cidade']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Bairro (NomeBairro, Regiao, CEP, ID_Cidade) VALUES (?, ?, ?, ?)',
                   (nome_bairro, regiao, cep, id_cidade))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Bairro created successfully'}), 201

# Route to get all Bairros
@app.route('/bairros', methods=['GET'])
def get_bairros():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Bairro')
    bairros = cursor.fetchall()
    conn.close()

    return jsonify([dict(bairro) for bairro in bairros])

# Route to get a specific Bairro by ID
@app.route('/bairro/<int:id>', methods=['GET'])
def get_bairro_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Bairro WHERE ID_Bairro = ?', (id,))
    bairro = cursor.fetchone()
    conn.close()

    if bairro is None:
        return jsonify({'message': 'Bairro not found'}), 404

    return jsonify(dict(bairro))

# Route to update an existing Bairro by ID
@app.route('/bairro/<int:id>', methods=['PUT'])
def update_bairro(id):
    data = request.get_json()
    nome_bairro = data['nome_bairro']
    regiao = data['regiao']
    cep = data['cep']
    id_cidade = data['id_cidade']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE Bairro SET NomeBairro = ?, Regiao = ?, CEP = ?, ID_Cidade = ? WHERE ID_Bairro = ?',
                   (nome_bairro, regiao, cep, id_cidade, id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Bairro updated successfully'})

# Route to delete a specific Bairro by ID
@app.route('/bairro/<int:id>', methods=['DELETE'])
def delete_bairro(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Bairro WHERE ID_Bairro = ?', (id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Bairro deleted successfully'})

# Route to create a new Logradouro
@app.route('/logradouro', methods=['POST'])
def create_logradouro():
    data = request.get_json()
    nome_rua = data['nome_rua']
    numero = data['numero']
    complemento = data['complemento']
    id_bairro = data['id_bairro']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Logradouro (NomeRua, Numero, Complemento, ID_Bairro) VALUES (?, ?, ?, ?)',
                   (nome_rua, numero, complemento, id_bairro))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Logradouro created successfully'}), 201

# Route to get all Logradouros
@app.route('/logradouros', methods=['GET'])
def get_logradouros():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Logradouro')
    logradouros = cursor.fetchall()
    conn.close()

    return jsonify([dict(logradouro) for logradouro in logradouros])

# Route to get a specific Logradouro by ID
@app.route('/logradouro/<int:id>', methods=['GET'])
def get_logradouro_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Logradouro WHERE ID_Logradouro = ?', (id,))
    logradouro = cursor.fetchone()
    conn.close()

    if logradouro is None:
        return jsonify({'message': 'Logradouro not found'}), 404

    return jsonify(dict(logradouro))

# Route to update an existing Logradouro by ID
@app.route('/logradouro/<int:id>', methods=['PUT'])
def update_logradouro(id):
    data = request.get_json()
    nome_rua = data['nome_rua']
    numero = data['numero']
    complemento = data['complemento']
    id_bairro = data['id_bairro']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE Logradouro SET NomeRua = ?, Numero = ?, Complemento = ?, ID_Bairro = ? WHERE ID_Logradouro = ?',
                   (nome_rua, numero, complemento, id_bairro, id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Logradouro updated successfully'})

# Route to delete a specific Logradouro by ID
@app.route('/logradouro/<int:id>', methods=['DELETE'])
def delete_logradouro(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Logradouro WHERE ID_Logradouro = ?', (id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Logradouro deleted successfully'})

# Similarly, you can create routes for Prefeitura and Usuario for CRUD operations.

# Route to create a new Prefeitura
@app.route('/prefeitura', methods=['POST'])
def create_prefeitura():
    data = request.get_json()
    nome_prefeitura = data['nome_prefeitura']
    contato = data['contato']
    endereco = data['endereco']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Prefeitura (NomePrefeitura, Contato, Endereco) VALUES (?, ?, ?)',
                   (nome_prefeitura, contato, endereco))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Prefeitura created successfully'}), 201

# Route to get all Prefeituras
@app.route('/prefeituras', methods=['GET'])
def get_prefeituras():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Prefeitura')
    prefeituras = cursor.fetchall()
    conn.close()

    return jsonify([dict(prefeitura) for prefeitura in prefeituras])

# Route to get a specific Prefeitura by ID
@app.route('/prefeitura/<int:id>', methods=['GET'])
def get_prefeitura_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Prefeitura WHERE ID_Prefeitura = ?', (id,))
    prefeitura = cursor.fetchone()
    conn.close()

    if prefeitura is None:
        return jsonify({'message': 'Prefeitura not found'}), 404

    return jsonify(dict(prefeitura))

# Route to update an existing Prefeitura by ID
@app.route('/prefeitura/<int:id>', methods=['PUT'])
def update_prefeitura(id):
    data = request.get_json()
    nome_prefeitura = data['nome_prefeitura']
    contato = data['contato']
    endereco = data['endereco']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE Prefeitura SET NomePrefeitura = ?, Contato = ?, Endereco = ? WHERE ID_Prefeitura = ?',
                   (nome_prefeitura, contato, endereco, id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Prefeitura updated successfully'})

# Route to delete a specific Prefeitura by ID
@app.route('/prefeitura/<int:id>', methods=['DELETE'])
def delete_prefeitura(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Prefeitura WHERE ID_Prefeitura = ?', (id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Prefeitura deleted successfully'})

# Route to create a new Usuario
@app.route('/usuario', methods=['POST'])
def create_usuario():
    data = request.get_json()
    nome_usuario = data['nome_usuario']
    email = data['email']
    telefone = data['telefone']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Usuario (NomeUsuario, Email, Telefone) VALUES (?, ?, ?)',
                   (nome_usuario, email, telefone))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Usuario created successfully'}), 201

# Route to get all Usuarios
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Usuario')
    usuarios = cursor.fetchall()
    conn.close()

    return jsonify([dict(usuario) for usuario in usuarios])

# Route to get a specific Usuario by ID
@app.route('/usuario/<int:id>', methods=['GET'])
def get_usuario_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Usuario WHERE ID_Usuario = ?', (id,))
    usuario = cursor.fetchone()
    conn.close()

    if usuario is None:
        return jsonify({'message': 'Usuario not found'}), 404

    return jsonify(dict(usuario))

# Route to update an existing Usuario by ID
@app.route('/usuario/<int:id>', methods=['PUT'])
def update_usuario(id):
    data = request.get_json()
    nome_usuario = data['nome_usuario']
    email = data['email']
    telefone = data['telefone']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE Usuario SET NomeUsuario = ?, Email = ?, Telefone = ? WHERE ID_Usuario = ?',
                   (nome_usuario, email, telefone, id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Usuario updated successfully'})

# Route to delete a specific Usuario by ID
@app.route('/usuario/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Usuario WHERE ID_Usuario = ?', (id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Usuario deleted successfully'})




# Similarly, you can create routes for Bairro, Logradouro, and Prefeitura for CRUD operations.

if __name__ == '__main__':
    app.run(debug=True)
