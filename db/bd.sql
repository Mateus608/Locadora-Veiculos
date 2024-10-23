CREATE DATABASE locadora;

USE locadora;

CREATE TABLE Pessoa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    endereco VARCHAR(255),
    tipo ENUM('Fisica', 'Juridica'),
    cpf VARCHAR(11),
    cnpj VARCHAR(14)
);

CREATE TABLE Veiculo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(255),
    marca VARCHAR(255),
    ano INT,
    tipo ENUM('CARRO', 'MOTO', 'CAMINHAO')
);

CREATE TABLE Aluguel (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pessoa_id INT,
    veiculo_id INT,
    dias INT,
    valor DECIMAL(10, 2),
    FOREIGN KEY (pessoa_id) REFERENCES Pessoa(id),
    FOREIGN KEY (veiculo_id) REFERENCES Veiculo(id)
);
