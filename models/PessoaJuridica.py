from models.Pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, nome, endereco, cnpj):
        super().__init__(nome, endereco)
        self._cnpj = cnpj

    def tipo_pessoa(self):
        return "Pessoa Jurídica"

    def __str__(self):
        return f"{super().__str__()}, CNPJ: {self._cnpj}"
