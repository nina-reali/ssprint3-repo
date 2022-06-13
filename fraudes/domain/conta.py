from numpy import random as rd
import numpy
from pycpfcnpj import gen

rd.seed(777)

class Conta:
    

    def __init__(self) -> None:
        self.cpf_cnpj, self.tipo_pessoa = self.generate_cpfCnpj()
        self.agencia = self.generate_agencia()
        # self.dispositivo = self.generate_dispositivo()
        # self.bloqueio, self.motivo_bloqueio = self.generate_bloqueio()
        self.limite_transacao = self.generate_limite(self.tipo_pessoa)
        # self.tempo_registro = self.generate_registro()


    def generate_cpfCnpj(self):
        indice = rd.choice(numpy.arange(0,2), p=[0.3,0.7])
        if indice == 0:
            return [self.get_cnpj(), "LEGAL_PERSON"]
        else:
            return [self.get_cnpj(), "NATURAL_PERSON"]

    def generate_agencia(self):
        array_agencias = ["0858", "0036", "0403", "0102", "0001"]
        indice = rd.choice(numpy.arange(0, 5), p=[0.1, 0.1, 0.1, 0.1, 0.6])
        return array_agencias[indice]

    def get_cpf(self):
        return rd.choice(["414.438.993-64", "563.770.497-06", "333.289.702-07", "363.733.588-36", "293.688.831-06", "268.620.150-95", "338.201.937-07", "831.792.100-01",
        "299.036.520-62", "872.295.475-98", "112.470.103-68", "298.503.791-38", "608.035.883-21", "078.890.882-05", "080.352.346-76", "281.019.093-38", "298.889.234-20", 
        "928.723.059-55", "166.819.546-18", "077.601.304-14", "057.404.502-33", "160.829.740-34"])

    


    def get_cnpj(self):
        return rd.choice(["72.501.511/2735-01", "73.478.140/4107-16", "90.518.132/9865-61", "72.500.770/8547-40", "07.421.260/5903-94", 
        "68.015.953/2692-98", "18.683.606/9968-09", "12.079.352/0246-90", "82.248.358/5147-16", "65.086.728/4320-07", "74.389.831/5513-69", 
        "44.091.697/9621-41", "38.978.086/6130-23"])


    # def generate_disposivo(self):
        

    # def generate_bloqueio(self):
    #     array_motivo_bloqueio = [
    #         "Suspeita de Fraude na Identidade do Correntista",
    #         "CPF Irregular",
    #         "Ordem Judicial",
    #         "Suspeita de Lavagem de Dinheiro",
    #         "Comprovação de Origem do Dinheiro",
    #         "Atividade Ilegal",
    #         "Sonegação de Impostos"
    #     ]

    #     indice = rd.choice(numpy.arrange(0,9), p=[0.3,0.2, 0.15, 0.05, 0.05, 0.05, 0.1, 0.1])
    #     if indice == 0:
    #         return [False,""]
    #     else:
    #         return [True,array_motivo_bloqueio[indice]]

    def generate_limite(self, tipo_pessoa):
        array_limite = [10,20,25,15,150,30,32,40,45]
        indice = rd.choice(numpy.arange(0,9), p=[0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])

        return array_limite[indice] * 100 if tipo_pessoa == "NATURAL_PERSON" else array_limite[indice] * 10000



    # def generate_registro(self):
