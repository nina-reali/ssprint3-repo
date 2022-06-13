from numpy import random as rd
import numpy
import phonenumbers
from phone_gen import PhoneNumber
import requests
import uuid
from datetime import date, timedelta

rd.seed(777)

class ChaveDict:

    def __init__(self, cpf_cnpj, nome_cliente) -> None:

        self.tipo_chave = self.obter_tipo_chave()
        self.chave_pix = cpf_cnpj if self.tipo_chave == "CPF" or self.tipo_chave == "CNPJ" else self.gerar_chave_pix_pelo_tipo(self.tipo_chave, nome_cliente) 
        self.reivindicada_doacao = self.obter_reivindicada_doacao()
        self.data_abertura = self.obter_data_abertura()
        self.data_posse = self.data_abertura if not self.reivindicada_doacao else self.obter_data_posse(self.data_abertura)
            

    def gerar_chave_pix_pelo_tipo(self, tipo_chave_pix, nome_cliente):

        switch = {
            "EVP": self.generate_uuid(),
            "PHONE": self.generate_phone_number(),
            "EMAIL": self.generate_email(nome_cliente)
        }

        return switch.get(tipo_chave_pix, "Tipo chave inexistente.")
    
    def obter_tipo_chave(self):
        array_tipos_chave = ["EMAIL", "PHONE", "EVP", "CPF", "CNPJ"]
        indice = rd.choice(numpy.arange(0,5), p=[0.3, 0.3, 0.2, 0.1, 0.1])
        return array_tipos_chave[indice]

    def generate_uuid(self):
        return str(uuid.uuid4())

    def generate_phone_number(self):

        phone_number = PhoneNumber("Brazil")

        telefone_formulario = phone_number.get_national()

        while len(telefone_formulario) <= 13:
            telefone_formulario = phone_number.get_mobile()

        telefone_formulario_ajustado = phonenumbers.parse(telefone_formulario, "BR")

        return phonenumbers.format_number(telefone_formulario_ajustado, phonenumbers.PhoneNumberFormat.NATIONAL)


    # def generate_email(self):
    #     for x in range(1):
    #         try:
    #             src = requests.get('https://emailfake.com').text
    #             emails = src.split('<span id="email_ch_text">')[1:]
    #             for email in emails:
    #                 valid = email[:30]
    #             return self.tratar_email(valid)
    #         except Exception:
    #             print("Connection Closed. We've been noticed boys!")

    # def tratar_email(self, email) -> str:
    #     email = email.strip('<span></span>')
    #     email = email.strip('</span>')
    #     email = email.strip('</b')
    #     email = email.strip('</span>')
    #     email = email.strip('</span></b><a h')
    #     email = email.strip('</span></b><a hr')
    #     return email

    def generate_email(self, nome_cliente):

        def obter_dominio():
            array_dominios = ["gmail.com", "yahoo.com", "icloud.com", "apple.com", "outlook.com", "sptech.school"]
            return str(rd.choice(array_dominios))

        nome_array = nome_cliente.split(" ")
        nome = f"{nome_array[0].lower()}.{nome_array[1].lower()}"
        return f"{nome}@{obter_dominio()}"

        

    def obter_reivindicada_doacao(self):
        array_doacao = [False, True]
        indice = rd.choice(numpy.arange(0, 2), p=[0.95, 0.05])
        return array_doacao[indice]

    def obter_data_abertura(self):
        data_hoje = date.today()
        rd.seed()
        data_random = data_hoje - timedelta(rd.randint(1, 200))
        return data_random
    
    def obter_data_posse(self, data_abertura):
        return data_abertura + timedelta(rd.randint(1,7)) # limite máximo para reivindicação/portabilidade
