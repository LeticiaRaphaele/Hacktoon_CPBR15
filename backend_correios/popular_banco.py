import os
import sqlite3
import random
import string

# Função para gerar um nome aleatório para cidades, bairros, etc.
def gerar_nome_aleatorio(tamanho=6):
    letras = string.ascii_lowercase
    return ''.join(random.choice(letras) for _ in range(tamanho)).capitalize()

# Função para popular as tabelas com dados fictícios
def popular_tabelas():
    # Conexão com o banco de dados
    db_path = os.path.join('db', 'base.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Populando a tabela Estado com alguns estados fictícios
    estados = [('São Paulo', 'SP'), ('Rio de Janeiro', 'RJ'), ('Minas Gerais', 'MG')]
    cursor.executemany('INSERT INTO Estado (NomeEstado, SiglaEstado) VALUES (?, ?)', estados)

    # Populando a tabela Cidade com algumas cidades fictícias
    cidades = [(gerar_nome_aleatorio(), random.randint(1000, 9999), 1),
               (gerar_nome_aleatorio(), random.randint(1000, 9999), 1),
               (gerar_nome_aleatorio(), random.randint(1000, 9999), 2),
               (gerar_nome_aleatorio(), random.randint(1000, 9999), 3)]
    cursor.executemany('INSERT INTO Cidade (NomeCidade, CodigoMunicipio, ID_Estado) VALUES (?, ?, ?)', cidades)

    # Populando a tabela Bairro com alguns bairros fictícios
    bairros = [(gerar_nome_aleatorio(), 'Centro', '12345678', 1),
               (gerar_nome_aleatorio(), 'Jardim', '87654321', 1),
               (gerar_nome_aleatorio(), 'Lapa', '56789012', 2)]
    cursor.executemany('INSERT INTO Bairro (NomeBairro, Regiao, CEP, ID_Cidade) VALUES (?, ?, ?, ?)', bairros)

    # Populando a tabela Logradouro com alguns logradouros fictícios
    logradouros = [(gerar_nome_aleatorio(), random.randint(1, 100), 'Sala A', 1),
                   (gerar_nome_aleatorio(), random.randint(1, 100), 'Apto 102', 2),
                   (gerar_nome_aleatorio(), random.randint(1, 100), '', 3)]
    cursor.executemany('INSERT INTO Logradouro (NomeRua, Numero, Complemento, ID_Bairro) VALUES (?, ?, ?, ?)', logradouros)

    # Populando a tabela Prefeitura com algumas prefeituras fictícias
    prefeituras = [(gerar_nome_aleatorio(), 'prefeitura1@example.com', 'Rua das Prefeituras, 123'),
                   (gerar_nome_aleatorio(), 'prefeitura2@example.com', 'Avenida dos Prefeitos, 456')]
    cursor.executemany('INSERT INTO Prefeitura (NomePrefeitura, Contato, Endereco) VALUES (?, ?, ?)', prefeituras)

    # Populando a tabela Usuario com alguns usuários fictícios
    usuarios = [(gerar_nome_aleatorio(), 'usuario1@example.com', '(11) 98765-4321'),
                (gerar_nome_aleatorio(), 'usuario2@example.com', '(21) 99876-5432'),
                (gerar_nome_aleatorio(), 'usuario3@example.com', '(31) 99999-0000')]
    cursor.executemany('INSERT INTO Usuario (NomeUsuario, Email, Telefone) VALUES (?, ?, ?)', usuarios)

    # Salvando as alterações e fechando a conexão
    conn.commit()
    conn.close()

if __name__ == "__main__":
    popular_tabelas()
    

