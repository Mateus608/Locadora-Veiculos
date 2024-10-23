from enum import Enum

class Veiculo:
    class TipoVeiculo(Enum):
        CARRO = 1
        MOTO = 2
        CAMINHAO = 3

    def __init__(self, modelo, marca, ano, tipo):
        self._modelo = modelo
        self._marca = marca
        self._ano = ano
        
        # Verifica se o tipo é uma instância da enumeração
        if isinstance(tipo, self.TipoVeiculo):
            self._tipo = tipo
        else:
            raise ValueError("Tipo deve ser uma instância de TipoVeiculo")

    def __str__(self):
        return f"Modelo: {self._modelo}, Marca: {self._marca}, Ano: {self._ano}, Tipo: {self._tipo.name}"
