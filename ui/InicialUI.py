from models.PessoaFisica import PessoaFisica
from models.PessoaJuridica import PessoaJuridica
from models.Veiculo import Veiculo
from models.Aluguel import Aluguel

class InicialUI:
    def __init__(self, db):
        self.db = db

    def menu(self):
        print("\n--- Menu Locadora de Veículos ---")
        print("1. Cadastrar Pessoa")
        print("2. Cadastrar Veículo")
        print("3. Realizar Aluguel")
        print("4. Sair")

    def cadastrar_pessoa(self):
        tipo = input("Digite o tipo de pessoa (1 para Física, 2 para Jurídica): ")
        nome = input("Nome: ")
        endereco = input("Endereço: ")
        
        if tipo == "1":
            cpf = input("CPF: ")
            pessoa = PessoaFisica(nome, endereco, cpf)
        elif tipo == "2":
            cnpj = input("CNPJ: ")
            pessoa = PessoaJuridica(nome, endereco, cnpj)
        else:
            print("Tipo inválido! A pessoa não será cadastrada.")
            return
        
        # Chama a função para inserir no banco de dados
        self.db.inserir_pessoa(pessoa)

    def cadastrar_veiculo(self):
        modelo = input("Modelo: ")
        marca = input("Marca: ")
        ano = int(input("Ano: "))
        
        print("Tipos de Veículo: 1. Carro, 2. Moto, 3. Caminhão")
        tipo_input = int(input("Escolha o tipo de veículo: "))

        # Mapeando a entrada do usuário para a enumeração
        tipo = None
        if tipo_input == 1:
            tipo = Veiculo.TipoVeiculo.CARRO
        elif tipo_input == 2:
            tipo = Veiculo.TipoVeiculo.MOTO
        elif tipo_input == 3:
            tipo = Veiculo.TipoVeiculo.CAMINHAO
        else:
            print("Tipo inválido! O veículo não será cadastrado.")
            return

        # Cria uma instância de Veiculo
        try:
            veiculo = Veiculo(modelo, marca, ano, tipo)
            # Chama a função para inserir no banco de dados
            self.db.inserir_veiculo(veiculo)
        except ValueError as e:
            print(f"Erro ao cadastrar veículo: {e}")

    def realizar_aluguel(self):
        try:
            pessoa_id = int(input("ID da pessoa: "))
            veiculo_id = int(input("ID do veículo: "))
            dias = int(input("Quantidade de dias: "))
            
            # Cria uma instância de Aluguel e insere no banco de dados
            aluguel = Aluguel(pessoa_id, veiculo_id, dias)
            self.db.inserir_aluguel(aluguel)
        except ValueError:
            print("Erro: Por favor, insira valores válidos para IDs e dias.")
