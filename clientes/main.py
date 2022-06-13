import email
import random as random
import gerador 
cpf=arquivo = open("./mocks/cpf_cnpj.txt", "r")
cpf = list(cpf)

for i in range(150000):

    ispb = random.choice(gerador.get_ispbs())
    banco = gerador.obter_nome_pelo_ispb(ispb)
    nome = gerador.GetPessoa().nome
    mail = gerador.GetPessoa().email
    cpfv=str(cpf[i]).strip()
    idade = gerador.GerarIdade(18,50)
    data = gerador.GerarData(idade)
    cep = gerador.GerarCep()
    valor = str(nome + ';' + cpfv + ';' + mail + ';' + banco + ';' + str(idade) + ';' + str(cep) + ';' + data )
    gerador.DefineArquivo(valor)

for i in range(50000):

    ispb = random.choice(gerador.get_ispbs())
    banco = gerador.obter_nome_pelo_ispb(ispb)
    nome = gerador.GetPessoa().nome
    mail = gerador.GetPessoa().email
    cpfv=str(cpf[i+150000]).strip()
    idade = gerador.GerarIdade(50,80)
    data = gerador.GerarData(idade)
    cep = gerador.GerarCep()
    valor = str(nome + ';' + cpfv + ';' + mail + ';' + banco + ';' + str(idade) + ';' + str(cep) + ';' + data )
    gerador.DefineArquivo(valor)