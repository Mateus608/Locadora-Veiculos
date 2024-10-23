from models.Pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, endereco, cpf):
        super().__init__(nome, endereco)
        self._cpf = cpf

    def tipo_pessoa(self):
        return "Pessoa Física"

    def __str__(self):
        return f"{super().__str__()}, CPF: {self._cpf}"
