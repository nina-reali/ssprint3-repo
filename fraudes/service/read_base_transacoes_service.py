import csv
from domain.transacao_dto import TransacaoDTO

class ReadBaseTransacoesService:

    def __init__(self) -> None:
        self.file_name = '../transacoes_pix.csv'

    def read(self):
        with open(self.file_name, mode='r') as csv_file:
            csvreader = csv.reader(csv_file)
            next(csvreader)
            transacoes = []
            for row in csvreader:
                transacoes.append(TransacaoDTO(row))

        return transacoes
            