from numpy import random as rd
import numpy
import names

rd.seed(777)

class Cliente:

    def __init__(self, cpf_cnpj, tipo_pessoa) -> None:
        self.cpf_cnpj, self.tipo_pessoa = cpf_cnpj, tipo_pessoa
        self.agencia = self.generate_agencia()
        self.conta = self.generate_conta()
        self.tipo_conta = self.obter_tipo_conta()
        self.nome = self.obter_nome_pessoa()
        self.nome_fantasia = self.obter_nome_fantasia(self.tipo_pessoa, self.nome)


    def generate_agencia(self):
        array_agencias = ["0858", "0036", "0403", "0102", "0001"]
        indice = rd.choice(numpy.arange(0, 5), p=[0.1, 0.1, 0.1, 0.1, 0.6])
        return array_agencias[indice]

    def generate_conta(self):
        conta = rd.randint(1000000, 9999999)
        digito = str(rd.randint(0,9))
        return f'{conta}-{digito}'

    def obter_tipo_conta(self):
        array_tipos_conta = ["CACC", "SLRY", "SVGS", "TRAN"]
        indice = rd.choice(numpy.arange(0,4), p=[0.5, 0.15, 0.2, 0.15])
        return array_tipos_conta[indice]

    def obter_nome_pessoa(self):
        return names.get_full_name()

    def obter_nome_fantasia(self, tipo_pessoa, nome):
        if tipo_pessoa == "LEGAL_PERSON":
            return nome + " LTDA"
        else:
            return ""