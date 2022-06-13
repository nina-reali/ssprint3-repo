import csv

class MakeCSV:

    def __init__(self, dict):
        self.mydict = dict
        self.fields = ['endToEnd','chave', 'tipoChave', 'instituicaoContraParte', 'nomeInstituicaoContraParte', 'tipoPessoaContraParte', 'instituicao', 'nomeInstituicao', 'tipoPessoa', 'valor', 'tipoIniciacao', 'siglaEstado', 'comentario',  'mes', 'dataTransacao', 'agendado', 'paisOrigem']

        self.filename = "../transacoes_pix.csv"

    def write(self):
        with open(self.filename, 'w') as csvfile: 
    # creating a csv dict writer object 
            writer = csv.DictWriter(csvfile, fieldnames = self.fields) 
                
            # writing headers (field names) 
            writer.writeheader() 
                
            # writing data rows 
            writer.writerows(self.mydict) 
    