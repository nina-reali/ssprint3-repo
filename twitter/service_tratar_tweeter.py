import re
from collections import namedtuple

class ServiceTratarTweeter:

    def __init__(self, twitters) -> None:
        self.twitters = twitters
        self.twitter_named_tuple = namedtuple("Twitter", ["id", "nome", "data", "texto"])

    def remover_quebra_de_linhas(self):
        twitters = []
        for tweet in self.twitters:
            texto = tweet.texto
            texto = str(tweet.texto).rstrip('\n')
            texto = texto.rstrip('\n')
            texto= texto.rstrip('\t')
            texto= texto.rstrip('\r')
            texto= texto.replace("\n","")
            texto = self.remover_emojis(texto)
            twitters.append(self.twitter_named_tuple(tweet.id, tweet.nome, tweet.data, texto))

        return twitters

    def remover_emojis(self, texto):

        def deEmojify(text):
            regrex_pattern = re.compile(pattern = "["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                "]+", flags = re.UNICODE)

            return regrex_pattern.sub(r'', text)

        return deEmojify(texto)
