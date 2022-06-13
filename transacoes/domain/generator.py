import random
#from readline import get_endidx
import uuid

import numpy
import phonenumbers
from phone_gen import PhoneNumber
from datetime import date, datetime, timedelta

random.seed(777)

class Generator:

    def generate_cpf():
        cpf = [random.randint(0, 9) for x in range(9)]                              
                                                                                
        for _ in range(2):                                                          
            val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11      
                                                                                    
            cpf.append(11 - val if val > 1 else 0)                                  
                                                                                
        return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)

    def generate_cnpj():
        def calculate_special_digit(l):                                             
            digit = 0                                                               
                                                                                    
            for i, v in enumerate(l):                                               
                digit += v * (i % 8 + 2)                                            
                                                                                    
            digit = 11 - digit % 11                                                 
                                                                                    
            return digit if digit < 10 else 0                                       
                                                                                    
        cnpj =  [1, 0, 0, 0] + [random.randint(0, 9) for x in range(8)]             
                                                                                    
        for _ in range(2):                                                          
            cnpj = [calculate_special_digit(cnpj)] + cnpj                           
                                                                                    
        return '%s%s.%s%s%s.%s%s%s/%s%s%s%s-%s%s' % tuple(cnpj[::-1])

    def generate_uuid():
        return str(uuid.uuid4())

    def generate_phone_number():

        phone_number = PhoneNumber("Brazil")
        
        telefone_formulario = phone_number.get_national()

        while len(telefone_formulario) <= 13:
            telefone_formulario = phone_number.get_mobile()

        telefone_formulario_ajustado = phonenumbers.parse(telefone_formulario, "BR")

        return phonenumbers.format_number(telefone_formulario_ajustado,phonenumbers.PhoneNumberFormat.NATIONAL)

    def generate_hora():
        hora = random.randint(00,23)
        minuto = str(random.randint(00,59))
        return [hora, minuto]

    def generate_date(agendado = None, mes = None, hora = None, minuto = None):

        array_datas = [2019, 2020, 2021, 2022]
        indice = numpy.random.choice(numpy.arange(0,4), p = [0.14, 0.19, 0.2, 0.47])

        date_now = date.today()
        day_date = date_now.strftime("%d")

        try:
            data_gerada = datetime(array_datas[indice], Generator.convert_stringmes_to_intmes(mes), int(day_date), int(hora), int(minuto), random.randint(0,59))
        except:
            data_gerada = datetime(array_datas[indice], Generator.convert_stringmes_to_intmes(mes), int(numpy.random.randint(1, 18)), int(hora), int(minuto), random.randint(0,59))

        if agendado == True:
            data_gerada = data_gerada + timedelta(days= numpy.random.randint(0,7))
        
        return data_gerada

    def get_transacao_agendada():
        array_agendada = [True, False]
        return array_agendada[numpy.random.choice(numpy.arange(0,2), p=[0.1, 0.9])]

    def convert_stringmes_to_intmes(mes):
        switch = {
            "JANEIRO": 1,
            "FEVEREIRO": 2,
            "MARÇO": 3,
            "ABRIL": 4,
            "MAIO": 5,
            "JUNHO": 6,
            "JULHO": 7,
            "AGOSTO": 8,
            "SETEMBRO": 9,
            "OUTUBRO": 10,
            "NOVEMBRO": 11,
            "DEZEMBRO": 12
        }

        return switch.get(mes, "Mês não encontrado.")

        
        

# Generator.generate_date()
