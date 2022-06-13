from numpy import random as rdpy
import random
from domain.mapa_brasil_coordenadas import GeolocalizaoBrasil

class Device:

    def __init__(self) -> None:
        self.device_name = self.generate_device_name()
        self.id_device = self.generate_id_device()
        self.geolocalizao_device = GeolocalizaoBrasil().geolocalizao

    def generate_device_name(self):
        return rdpy.choice(["iPhone 13 Pro MAX","iPhone 12", "Samsung Galaxy S21", "Samsung Galaxy S20", 
        "Motorola Edge Plus 5G", "Xiaomi Mi 10T 5G", "Motorola One Zoom", "Samsung Galaxy A80",
        "Asus ROG Phone 5", "iPhone 13 Mini", "Samsung Galaxy M62"])

    def generate_id_device(self):
        array_devices = ["H132S01N2O85", "G883C08K0H88", "V376F07Y4B90", "Z987W01O8U89", "X674Y07M3N87", "H793R07X4I85", "W716L06K8O90", "G676K04O2D85", "T359J02Q6C98", "D239I06N8V93", "T683M05L4J90", "J742P03E2A80", "C113U06D5O96", "D308Q01V3T88", "V738L06D6J80", "J103K03T4Q89", "S542B06Q2O92", "G553P08I8V82", "I180S01K1R82", "B372T06B1E97", "N674Y06W7B80", "K972M08W1S84", "K470G07R1I90", "F354N05O5F81", "U331B07D8Z97", "D283V02K1R81", "G989O02H5N92", "Q640M07L0Q86", "M438U02Q1K94", "Z287T00K6A91", "Q581K08Z7E89", "I670I05L7I85", "D225E02E1J98", "E821O08B3X87", "O802I04T1I82", "Q361W05M0A85"]
        return rdpy.choice(array_devices)

        # letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # indice_letra = rdpy.randint(0, len(letras))
        # indice_segunda_letra = rdpy.randint(0, len(letras))
        # indice_terceira_letra = rdpy.randint(0, len(letras))
        # indice_quarta_letra = rdpy.randint(0, len(letras))
        # id_device = f"{letras[indice_letra]}{rdpy.randint(100, 999)}{letras[indice_segunda_letra]}0{rdpy.randint(0,9)}{letras[indice_terceira_letra]}{rdpy.randint(0,9)}{letras[indice_quarta_letra]}{rdpy.randint(80, 99)}"
        # return id_device
        
    