from numpy import random
from collections import namedtuple

class GeolocalizaoBrasil:

    def __init__(self) -> None:
        geo = self.get_geolocalizao()
        latitude, longitude = geo['coordenadas']
        self.geolocalizao = {
            'cidade': geo['cidade'],
            'latitude': latitude,
            'longitude': longitude
        }

    def get_geolocalizao(self):
        Geolocalizacao = namedtuple("Geolocalizacao", ["Cidade", "latitude", "longitude"])
        
        array_geolocalizacoes = [
            Geolocalizacao("Belo Horizonte", -19.9248772, -43.9360843),
            Geolocalizacao("São Paulo", -23.5573527, -46.6611003),
            Geolocalizacao("Rio de Janeiro", -22.9811559, -43.2027176),
            Geolocalizacao("Fortaleza", -12.973234, -38.5085446),
            Geolocalizacao("João Pessoa", -7.1141673, -34.8322773),
            Geolocalizacao("Salvador", -3.7401015, -38.4782827)
        ]

        local = array_geolocalizacoes[random.randint(0, 6)]
        return {'cidade': local.Cidade, 'coordenadas': [local.latitude, local.longitude]}
