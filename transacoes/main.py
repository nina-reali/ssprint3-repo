from domain.contexto_bancario import TransferenciaPIX, Instituicao
import random
from service.transferencia_pix_service import MakeCSV
from tqdm import tqdm
from service.read_base_pessoa import ReadBasePessoa

random.seed(777)

transacoes = []

base_pessoa = ReadBasePessoa().read()
lista_tipos_pessoa = Instituicao.get_tipos_pessoa()
lista_tipos_chave_pix = Instituicao.get_tipos_chaves_pix()
lista_siglas=Instituicao.get_siglas_estados()
descricao=Instituicao.verdadeiro()

for i in tqdm (range(0, 25_000), desc="Inserindo dados...", ascii=False, ncols=100):
    valor = round(random.uniform(100_000,9_999_999),2)
    tipo_pessoa_debitante = random.choice(lista_tipos_pessoa)
    instituicao_debitante = Instituicao.get_ispbs()
    tipo_chave_pix = random.choice(lista_tipos_chave_pix)
    siglas= random.choice(lista_siglas)
    informacao_entre_usuarios = random.choice(descricao)
    instituicao_creditante = Instituicao.get_ispbs()

    transacoes.append(TransferenciaPIX(base_pessoa[i].documento, valor, tipo_pessoa_debitante, instituicao_debitante, tipo_chave_pix, siglas,informacao_entre_usuarios, instituicao_creditante).get_transferencia())


for i in tqdm (range(25_000, 100_099), desc="Inserindo dados...", ascii=False, ncols=100):
    valor = round(random.uniform(10,50_000),2)
    tipo_pessoa_debitante = random.choice(lista_tipos_pessoa)
    instituicao_debitante = Instituicao.get_ispbs()
    tipo_chave_pix = random.choice(lista_tipos_chave_pix)
    siglas = random.choice(lista_siglas)
    informacao_entre_usuarios = random.choice(descricao)
    instituicao_creditante = Instituicao.get_ispbs()
    transacoes.append(TransferenciaPIX(base_pessoa[i].documento, valor, tipo_pessoa_debitante, instituicao_debitante, tipo_chave_pix, siglas, informacao_entre_usuarios, instituicao_creditante).get_transferencia())

make_csv = MakeCSV(transacoes)
make_csv.write()

