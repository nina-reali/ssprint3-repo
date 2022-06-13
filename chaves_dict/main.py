from service.create_base_dict_service import CreateBaseDict
from service.create_xml_service import CreateXMLService
from tqdm import tqdm

array_dict = []

for linha in tqdm(open("./mocks/cpf_cnpj.txt", "r").readlines(), desc="Gerando massa de dados...", ascii=False, ncols=100):
    cpf_cnpj, tipo_pessoa = linha.split(",")
    array_dict.append(CreateBaseDict(cpf_cnpj = cpf_cnpj, tipo_pessoa = tipo_pessoa))

createXML = CreateXMLService(array_dict)
createXML.write_xml()