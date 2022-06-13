from random import seed
from service.create_base_dict_service import CreateBaseFraude
from service.create_json_service import CreateJsonService
from service.read_base_transacoes_service import ReadBaseTransacoesService
from service.read_base_pessoa import ReadBasePessoa
from tqdm import tqdm
import domain.bloqueio as bloqueio

seed(777)
array_fraudes = []
base_transacoes = ReadBaseTransacoesService()
transacoes = base_transacoes.read()
base_pessoas = ReadBasePessoa()
pessoas = base_pessoas.read()


def validar_transaco(device_id, documento, agencia, localizacao, datetime_transacao):
    for fraude in array_fraudes:
        if device_id != fraude["device"]["id"] and documento == fraude["documento"] and agencia == fraude["agencia"]:
            return [True, bloqueio.SUSPEITA_DEVICE_DIFERENTE]

        if localizacao != fraude["device"]["geolocalizacao"]["cidade"] and documento == fraude["documento"] and agencia == fraude["agencia"]: 
            if datetime_transacao.hour - fraude["dataTransacao"].hour >= 5:
                return [True, bloqueio.SUSPEITA_LOCAL_TRANSACAO]
        
        
    
    return [False, ""]



for i in tqdm(range(0, len(transacoes)), desc="Gerando massa de dados...", ascii=False, ncols=100):
    dado_gerado_fraude = CreateBaseFraude(transacoes[i], pessoas[i])
    suspeito, motivo = validar_transaco(dado_gerado_fraude.dict["device"]["id"], 
    dado_gerado_fraude.dict["documento"], dado_gerado_fraude.dict["agencia"], 
    dado_gerado_fraude.dict["device"]["geolocalizacao"], 
    dado_gerado_fraude.dict["dataTransacao"])
    if suspeito == True:
        array_fraudes.append(dado_gerado_fraude.set_motivo_bloqueio(motivo).dict)
    else:
        array_fraudes.append(dado_gerado_fraude.dict)


fraudes_confirmadas = []
for fraude in array_fraudes:
    if fraude["status_transacao"] == "RECUSADO":
        fraudes_confirmadas.append(fraude)

createJson = CreateJsonService(fraudes_confirmadas)
createJson.write()