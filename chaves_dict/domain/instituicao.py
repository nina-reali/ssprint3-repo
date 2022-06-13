from numpy import random as rd
import numpy

rd.seed(777)

class Instituicao:

    def __init__(self, tipo_pessoa) -> None:
        self.ispb, self.nome_ispb = self.obter_ispb_e_nome(tipo_pessoa)

    def obter_ispb_e_nome(self, tipo_pessoa):
        array_insitituicoes_digitais = [["18236120", "NU PAGAMENTOS S.A."], ["31872495", "Banco C6 S.A."], ["00416968", "Banco Inter S.A."]]
        array_instituicoes_tradicionais = [["58160789", "Banco Safra S.A."], ["90400888", "BANCO SANTANDER (BRASIL) S.A."]]

        if tipo_pessoa == "NATURAL_PERSON":
            indice = rd.choice(numpy.arange(0,3), p=[0.5, 0.25, 0.25])
            return array_insitituicoes_digitais[indice]
        else:
            indice = rd.choice(numpy.arange(0,2), p=[0.6, 0.4])
            return array_instituicoes_tradicionais[indice]

        