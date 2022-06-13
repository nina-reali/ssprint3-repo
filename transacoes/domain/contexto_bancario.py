from re import A
from domain.generator import Generator
import random
from numpy import indices, random as rd
import numpy
import string

random.seed(777)

class TransferenciaPIX:

    def __init__(self, cpf_cnpj = None, valor = None, tipo_pessoa_debitante = None, instituicao_debitante = None, tipo_chave = None, sigla = None, descricao = None,  instituicao_creditante = None):
        hora, minuto = Generator.generate_hora()
        agendado = Generator.get_transacao_agendada()
        mes = Instituicao.mes_uteis()
        dia = Instituicao.dias_uteis_pix()
        data = Generator.generate_date(agendado = agendado, mes = mes, hora = hora, minuto=minuto)
        self.transferencia = dict({
            'endToEnd': self.gerar_end_to_end(data_transacao = data, ispb = instituicao_creditante),
            'chave': self.gerar_chave_pix_pelo_tipo(tipo_chave_pix = tipo_chave, cpf_cnpj = cpf_cnpj),
            'tipoChave': tipo_chave,
            'instituicaoContraParte': instituicao_debitante,
            'nomeInstituicaoContraParte': Instituicao.obter_nome_pelo_ispb(instituicao_debitante),
            'tipoPessoaContraParte': tipo_pessoa_debitante,
            'instituicao': instituicao_creditante,
            'nomeInstituicao': Instituicao.obter_nome_pelo_ispb(instituicao_creditante),
            'tipoPessoa': self.obter_tipo_pessoa_creditante(tipo_chave = tipo_chave),
            'valor': self.obter_valor_baseado_hora(hora, valor),
            'tipoIniciacao': self.obter_tipo_iniciacao(tipo_chave),
            'siglaEstado': sigla,
            'comentario': descricao,
            'mes': mes,
            'dataTransacao': str(data),
            'agendado': agendado,
            'paisOrigem': 'Brazil'
        })

    def __str__(self) -> str:
        return str(self.transferencia)


    def obter_tipo_iniciacao(self, tipo_chave):

        if tipo_chave == "EVP":
            return "QR_CODE"
        
        return Instituicao.get_tipos_iniciacao()


    def gerar_chave_pix_pelo_tipo(self, tipo_chave_pix, cpf_cnpj):
        switch = {
            "CPF": cpf_cnpj,
            "CNPJ": cpf_cnpj,
            "EVP": Generator.generate_uuid(),
            "PHONE": Generator.generate_phone_number()
        }

        return switch.get(tipo_chave_pix, "Tipo chave inexistente.")

    def obter_tipo_pessoa_creditante(self, tipo_chave):

        if tipo_chave == "CPF":
            return "NATURAL_PERSON"

        if tipo_chave == "CNPJ":
            return "LEGAL_PERSON"

        return random.choice(["PJ", "PF"])

    def obter_valor_baseado_hora(self, hora, valor):
        if hora <= 6 or hora >= 23:
            valor = round(random.uniform(1,1000),2)

        return valor

    def get_transferencia(self):
        return self.transferencia

    def get_instituicao(self):
        return self.transferencia['instituicao_debitante']

    def gerar_end_to_end(self, data_transacao, ispb):

        def random_caracters(size=6, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))


        return f'E{ispb}{data_transacao.strftime("%Y%m%d")}{random_caracters()}'


class Instituicao:

    def get_ispbs():
        array_ispbs = ["18236120", "31872495", "58160789", "90400888", "00416968"]
        indice = rd.choice(numpy.arange(0, 5), p=[0.23, 0.2, 0.1, 0.25, 0.22])
        return array_ispbs[indice]


    def get_tipos_pessoa():
        return ["PJ", "PF"]

    def get_tipos_iniciacao():
        array_tipos_iniciacao = ["CHAVE", "DEVOLUCAO", "MANUAL"]
        return array_tipos_iniciacao[rd.choice(numpy.arange(0,3), p = [0.62, 0.08, 0.3])]
        

    def obter_nome_pelo_ispb(ispb):
        switch = {
            "18236120": "NU PAGAMENTOS S.A.",
            "31872495": "Banco C6 S.A.",
            "58160789": "Banco Safra S.A.",
            "90400888": "BANCO SANTANDER (BRASIL) S.A.",
            "00416968": "Banco Inter S.A."
        }

        return switch.get(ispb, "Instituição não encontrada.")

    def status_envio_transacoes_pix():
        return ["ENVIADA", "EFETIVADA", "RECUSADA", "ERRO", "CANCELADA"]

    def get_tipos_chaves_pix():
        return ["CPF","CNPJ", "EVP", "PHONE"]

    def verdadeiro():
        return  [True, False]
        
    
    def get_siglas_estados():
        return ["AC", "AL" ,"AM" ,"AP" ,"BA","CE" ,"DF"  ,"ES"  ,"GO" ,"MA" ,"MG"  ,"MS"  ,"MT"  ,"PA" ,"PB" ,"PE" ,"PI" ,"PR" ,"RJ"  ,"RN"  ,"RO" ,"RR" ,"RS"  ,"SC"  ,"SE" ,"SP" ,"TO"]

    def dias_uteis_pix():
        array_dias =  [
            "DOMINGO",
            "SEGUNDA",
            "TERÇA-FEIRA",
            "QUARTA-FEIRA",
            "QUINTA-FEIRA",
            "SEXTA-FEIRA",
            "SÁBADO"
        ]

        indice = rd.choice(numpy.arange(0,7), p=[0.1, 0.07, 0.2, 0.13, 0.16, 0.23, 0.11])
        return array_dias[indice]

    def mes_uteis():
        array_meses = [
            "JANEIRO",
            "FEVEREIRO",
            "MARÇO",
            "ABRIL",
            "MAIO",
            "JUNHO",
            "JULHO",
            "AGOSTO",
            "SETEMBRO",
            "OUTUBRO",
            "NOVEMBRO",
            "DEZEMBRO"
        ]

        indice = rd.choice(numpy.arange(0,12) , p=[9.5/100, 6/100, 8.5/100, 7/100, 9/100, 8/100, 8.5/100, 7/100, 7/100, 8.5/100, 9/100, 12/100]) # probabilidade
        return array_meses[indice]

    def obter_estado_pela_sigla(sigla):
        switch = {
            "AC" : "Acre",
            "AL" : "Alagoas",
            "AM" : "Amazonas",
            "AP" : "Amapá",
            "BA" : "Bahia",
            "CE" : "Ceará",
            "DF" : "Distrito Federal",
            "ES" : "Espirito Santo",
            "GO" : "Goiás",
            "MA" : "Maranhão",
            "MG" : "Minas Gerais",
            "MS" : "Mato Grosso do Sul",
            "MT" : "Mato Grosso",
            "PA" : "Pará",
            "PB" : "Paraíba",
            "PE" : "Pernambuco",
            "PI" : "Piauí",
            "PR" : "Paraná",
            "RJ" : "Rio de Janeiro",
            "RN" : "Rio Grande do Norte",
            "RO" : "Rondônia",
            "RR" : "Roraima",
            "RS" : "Rio Grande do Sul",
            "SC" : "Santa Catarina",
            "SE" : "Sergipe",
            "SP" : "Sao Paulo",
            "TO" : "Tocantins"
        }

        return switch.get(sigla, "Estado não encontrado")