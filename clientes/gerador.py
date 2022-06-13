from faker import Faker
import random as random
import pessoa as Pessoa
from datetime import date
fake = Faker()
pessoa = Pessoa

def GetPessoa():

         
    pes=pessoa.pessoa(fake.name(),fake.email())
    return pes

def DefineArquivo(pessoa):
    
    
    try:
        nome_arquivo = '../pessoa.txt'
        arquivo = open(nome_arquivo, 'r+')
        texto = arquivo.readlines()
        texto.append('2')
        arquivo.writelines("\n"+str(pessoa))
    except FileNotFoundError:
        arquivo = open(nome_arquivo, 'w+')
        arquivo.writelines('nome-cpf-email-banco-idade-cep-dataNascimento' )
        arquivo.writelines("\n"+str(pessoa))
    arquivo.close()
                                                     
    

def GerarIdade(min,max):
    idade = random.randint(min,max)
    return idade

def get_ispbs():
    return ["18236120", "31872495", "58160789", "90400888", "00416968","60872504"]

def obter_nome_pelo_ispb(ispb):
    switch = {
        "18236120": "NU PAGAMENTOS S.A.",
        "31872495": "Banco C6 S.A.",
        "58160789": "Banco Safra S.A.",
        "90400888": "BANCO SANTANDER (BRASIL) S.A.",
        "00416968": "Banco Inter S.A.",
        "60872504": "Banco ITAÚ S.A"
    }

    return switch.get(ispb, "InstituiÃ§Ã£o nÃ£o encontrada.")


def GerarCep():                                                        
    cep = [random.randint(0, 9) for x in range(6)]                              
                                                                                
    for _ in range(2):                                                          
        val = sum([(len(cep) + 1 - i) * v for i, v in enumerate(cep)]) % 8      
                                                                                
        cep.append(8 - val if val > 1 else 0)                                  
                                                                                
    return '%s%s%s%s%s%s%s%s' % tuple(cep)
    
def GerarQtdChaves():
    chaves = random.randint(1,3)
    return chaves


def GerarData(idade):
    data = date.today()
    dia = random.randint(1,31)
    mes = random.randint(1,12)
    ano = data.year - idade
    dataFinal = str(dia) + "/" + str(mes) + "/" + str(ano)
    return dataFinal