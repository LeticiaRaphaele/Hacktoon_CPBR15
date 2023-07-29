-- Criação das tabelas do Banco de Dados
CREATE TABLE Estado (
    ID_Estado INT AUTO_INCREMENT PRIMARY KEY,
    NomeEstado VARCHAR(100) NOT NULL,
    SiglaEstado VARCHAR(2) NOT NULL
);

CREATE TABLE Cidade (
    ID_Cidade INT AUTO_INCREMENT PRIMARY KEY,
    NomeCidade VARCHAR(255) NOT NULL,
    CodigoMunicipio INT,
    ID_Estado INT,
    FOREIGN KEY (ID_Estado) REFERENCES Estado(ID_Estado)
);

CREATE TABLE Bairro (
    ID_Bairro INT AUTO_INCREMENT PRIMARY KEY,
    NomeBairro VARCHAR(255) NOT NULL,
    Regiao VARCHAR(100),
    CEP VARCHAR(8),
    ID_Cidade INT,
    FOREIGN KEY (ID_Cidade) REFERENCES Cidade(ID_Cidade)
);

CREATE TABLE Logradouro (
    ID_Logradouro INT AUTO_INCREMENT PRIMARY KEY,
    NomeRua VARCHAR(255) NOT NULL,
    Numero INT,
    Complemento VARCHAR(100),
    ID_Bairro INT,
    FOREIGN KEY (ID_Bairro) REFERENCES Bairro(ID_Bairro)
);

CREATE TABLE Prefeitura (
    ID_Prefeitura INT AUTO_INCREMENT PRIMARY KEY,
    NomePrefeitura VARCHAR(255) NOT NULL,
    Contato VARCHAR(100),
    Endereco VARCHAR(255)
);

CREATE TABLE Usuario (
    ID_Usuario INT AUTO_INCREMENT PRIMARY KEY,
    NomeUsuario VARCHAR(255) NOT NULL,
    Email VARCHAR(100),
    Telefone VARCHAR(20)
);
