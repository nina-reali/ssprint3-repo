from numpy import random as rd
import numpy
from faker import Faker

rd.seed(777)

class Transacao:

    def __init__(self, limite_transacao, valor, data) -> None:
        self.transacoes_ultima_hora = self.generate_quantidade()
        self.valor = valor
        self.valor_medio = self.generate_valor_medio(limite_transacao,self.transacoes_ultima_hora)
        self.status_transacao = self.generate_status(self.transacoes_ultima_hora,self.valor,limite_transacao,self.valor_medio)
        self.data_transacao = data

    def generate_quantidade(self):
        indice = rd.choice(numpy.arange(1,6), p=[0.3, 0.3, 0.2, 0.1, 0.1])
        return indice

    def generate_valor(self, limite_transacao):
        indice = rd.choice(numpy.arange(0,2), p=[0.3, 0.7])
        if indice == 0:
            valor = round(rd.randint(1,limite_transacao),2)
            return valor
        else:
            valor = round(rd.randint(1,limite_transacao),2)
            return valor

    def generate_valor_medio(self, limite_transacao, quantidade):
        valor = round(rd.randint(1,limite_transacao),2)
        media = (valor + limite_transacao * 2)/quantidade 
        return media

    def generate_status(self, quantidade, valor, limite_transacao, valor_medio):
        if quantidade > 5 or float(valor) > limite_transacao or (float(valor) * 0.7) > valor_medio:
            return "RECUSADO"
        else:
            return "APROVADO"
