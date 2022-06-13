import datetime
from random import seed
from domain.conta import Conta
from domain.transacao import Transacao
from domain.device import Device
import domain.bloqueio as bloqueio

seed(777)

class CreateBaseFraude:

    def __init__(self, transacao_dto = None, pessoa = None) -> None:

        conta = Conta()
        transacao = Transacao(conta.limite_transacao, transacao_dto.valor, transacao_dto.data_transacao)
        device = Device()

        motivos_bloqueio = []

        if conta.cpf_cnpj in bloqueio.CPFS_CNPJS_BLOQUEADOS_ORDEM_JUDICIAL:
            motivos_bloqueio.append(bloqueio.ORDEM_JUDICIAL)
        if conta.cpf_cnpj in bloqueio.CNPJS_BLOQUEADOS_SUSPEITA_ORIGEM_DINHEIRO:
            motivos_bloqueio.append(bloqueio.SUSPEITA_ORIGEM_DINHEIRO)
        if conta.cpf_cnpj in bloqueio.CONTAS_BLOQUEADAS_23:
            motivos_bloqueio.append(bloqueio.BLOQUEADAS_23)

        self.dict = {
            "endToEnd": transacao_dto.end_to_end,
            "documento": pessoa.documento,
            "tipo_pessoa": conta.tipo_pessoa,
            "agencia": conta.agencia,
            "limite_transacao":float(conta.limite_transacao),
            "valor":float(transacao.valor),
            "status_transacao": "RECUSADO" if len(motivos_bloqueio) > 0 else transacao.status_transacao,
            "transacao_ultima_hora": int(transacao.transacoes_ultima_hora),
            "dataTransacao": datetime.datetime.strptime(transacao_dto.data_transacao, "%Y-%m-%d %H:%M:%S"),
            "device": {
                "id": device.id_device,
                "name": device.device_name,
                "geolocalizacao": device.geolocalizao_device
            },
            "motivosBloqueio": motivos_bloqueio
        }

    def set_motivo_bloqueio(self, motivo_bloqueio):
        self.dict["motivosBloqueio"].append(motivo_bloqueio)
        self.dict["status_transacao"] = "RECUSADO"
        return self

    