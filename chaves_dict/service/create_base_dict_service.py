from domain.chave_dict import ChaveDict
from domain.cliente import Cliente
from domain.instituicao import Instituicao

class CreateBaseDict:

    def __init__(self, cpf_cnpj, tipo_pessoa) -> None:

        cliente = Cliente(cpf_cnpj = cpf_cnpj, tipo_pessoa = tipo_pessoa)
        instituicao = Instituicao(cliente.tipo_pessoa)
        chave = ChaveDict(cliente.cpf_cnpj, cliente.nome)
        
        self.dict = {
            "agencia": cliente.agencia,
            "conta": cliente.conta,
            "cpfCnpj": cliente.cpf_cnpj,
            "Instituicao": instituicao.ispb,
            "tipoConta": cliente.tipo_conta,
            "nome": cliente.nome,
            "tipoPessoa": cliente.tipo_pessoa,
            "chave": chave.chave_pix,
            "tipoChave": chave.tipo_chave,
            "dataAbertura": chave.data_abertura.strftime('%Y-%m-%dT%H:%M:%S'),
            "dataPosse": chave.data_posse.strftime('%Y-%m-%dT%H:%M:%S'),
            "nomeFantasia": cliente.nome_fantasia,
            "reivindicadaDoacao": chave.reivindicada_doacao,
            "nomePSP": instituicao.nome_ispb
        }

    def __str__(self):
        return self.dict
