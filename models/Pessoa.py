from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco

    @abstractmethod
    def tipo_pessoa(self):
        pass

    def __str__(self):
        return f"Nome: {self._nome}, Endereço: {self._endereco}"
