import xml.etree.ElementTree as ET
from tqdm import tqdm

class CreateXMLService:

    def __init__(self, array_dict) -> None:
        self.array_dict = array_dict

    def write_xml(self):
        asset = ET.Element('Asset')
        asset.set('type', 'Array[]')

        key_list = list(self.array_dict[0].dict.keys())

        def obter_texto(valor):
            if valor == True:
                return 'True'
            elif valor == False:
                return 'False/'
            else:
                return valor

        for indice_array in tqdm(range(len(self.array_dict)), desc="Escrevendo arquivo XML...", ascii=False, ncols=100):
            elemento_pai = ET.SubElement(asset, 'dict')
            val_list = list(self.array_dict[indice_array].dict.values())

            for indice in range(len(val_list)):
                element = ET.SubElement(elemento_pai, key_list[indice])
                element.text = obter_texto(valor = val_list[indice])

        dict_string_xml = ET.tostring(asset)
        with open("../DICT.xml", "wb") as f:
            f.write(dict_string_xml)

