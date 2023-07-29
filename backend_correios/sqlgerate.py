import os
import sqlite3

# Função para criar as tabelas usando o script SQL
def criar_tabelas():
    # Verifica se a pasta /db existe, caso contrário, cria-a
    if not os.path.exists('db'):
        os.makedirs('db')

    # Conexão com o banco de dados (será criado em /db se não existir)
    db_path = os.path.join('db', 'base.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Script SQL com a criação das tabelas
    script_sql = '''
    -- Criação das tabelas do Banco de Dados
    CREATE TABLE Estado (
        ID_Estado INTEGER PRIMARY KEY AUTOINCREMENT,
        NomeEstado VARCHAR(100) NOT NULL,
        SiglaEstado VARCHAR(2) NOT NULL
    );

    CREATE TABLE Cidade (
        ID_Cidade INTEGER PRIMARY KEY AUTOINCREMENT,
        NomeCidade VARCHAR(255) NOT NULL,
        CodigoMunicipio INTEGER,
        ID_Estado INTEGER,
        FOREIGN KEY (ID_Estado) REFERENCES Estado(ID_Estado)
    );

    CREATE TABLE Bairro (
        ID_Bairro INTEGER PRIMARY KEY AUTOINCREMENT,
        NomeBairro VARCHAR(255) NOT NULL,
        Regiao VARCHAR(100),
        CEP VARCHAR(8),
        ID_Cidade INTEGER,
        FOREIGN KEY (ID_Cidade) REFERENCES Cidade(ID_Cidade)
    );

    CREATE TABLE Logradouro (
        ID_Logradouro INTEGER PRIMARY KEY AUTOINCREMENT,
        NomeRua VARCHAR(255) NOT NULL,
        Numero INTEGER,
        Complemento VARCHAR(100),
        ID_Bairro INTEGER,
        FOREIGN KEY (ID_Bairro) REFERENCES Bairro(ID_Bairro)
    );

    CREATE TABLE Prefeitura (
        ID_Prefeitura INTEGER PRIMARY KEY AUTOINCREMENT,
        NomePrefeitura VARCHAR(255) NOT NULL,
        Contato VARCHAR(100),
        Endereco VARCHAR(255)
    );

    CREATE TABLE Usuario (
        ID_Usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        NomeUsuario VARCHAR(255) NOT NULL,
        Email VARCHAR(100),
        Telefone VARCHAR(20)
    );
    '''

    # Executando o script SQL
    cursor.executescript(script_sql)

    # Salvando as alterações e fechando a conexão
    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_tabelas()
