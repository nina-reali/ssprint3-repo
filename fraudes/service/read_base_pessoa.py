from domain.pessoa_dto import PessoaDTO

class ReadBasePessoa:
    
    def __init__(self) -> None:
        self.file_name = "../pessoa.txt"

    def read(self):
        pessoas = []
        with open(self.file_name) as f:
            next(f)
            while True:
                line = f.readline()
                if not line:
                    break
                pessoas.append(PessoaDTO(line.replace("\n","").split(";")))
        
        return pessoas