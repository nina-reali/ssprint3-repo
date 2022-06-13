class PessoaDTO:
    
    def __init__(self, array_parser) -> None:
        self.nome = array_parser[0]
        self.documento = array_parser[1]
        self.email = array_parser[2]
        self.banco = array_parser[3]
        self.idade = array_parser[4]
        self.cep = array_parser[5]
        self.data_nascimento = array_parser[6]