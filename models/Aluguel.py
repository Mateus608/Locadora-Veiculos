class Aluguel:
    def __init__(self, pessoa_id, veiculo_id, dias):
        self._pessoa_id = pessoa_id
        self._veiculo_id = veiculo_id
        self._dias = dias

    def calcular_valor(self):
        # A lógica de cálculo pode ser melhorada com base no tipo do veículo.
        # Aqui, estamos apenas simulando o cálculo.
        if self._veiculo_id == 1:  # Exemplo: ID de um carro
            return 100 * self._dias
        elif self._veiculo_id == 2:  # Exemplo: ID de uma moto
            return 50 * self._dias
        elif self._veiculo_id == 3:  # Exemplo: ID de um caminhão
            return 200 * self._dias
        return 0

    def __str__(self):
        return f"Aluguel: Pessoa ID {self._pessoa_id}, Veículo ID {self._veiculo_id}, Dias: {self._dias}, Valor: {self.calcular_valor()}"
