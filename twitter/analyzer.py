class Analyzer:

    def __init__(self, tweets) -> None:
        self.tweets = tweets

    def filtrar_tweets(self):
        adverbios_negacao = []
        substantivos_negativos = []
        adverbios_positivos = []
        with open('./words/adverbios_negacao.txt') as f:
            lines = f.readlines()
            for line in lines:
                adverbios_negacao.append(line.replace("\n", ""))

        with open('./words/substantivos_negacao.txt') as f:
            lines = f.readlines()
            for line in lines:
                substantivos_negativos.append(line.replace("\n", ""))

        with open('./words/adverbios_positivos.txt') as f:
            lines = f.readlines()
            for line in lines:
                adverbios_positivos.append(line.replace("\n", ""))

        twitter_positivos = []
        twitters_negativos = []
        twitters_neutros = []
        for twitter in self.tweets:
            texto = twitter.texto.split(" ")

            if any(palavra in adverbios_negacao for palavra in texto):
                twitters_negativos.append(twitter)
            elif any(palavra in substantivos_negativos for palavra in texto):
                twitters_negativos.append(twitter)
            elif any(palavra in adverbios_positivos for palavra in texto):
                twitter_positivos.append(twitter)
            else:
                twitters_neutros.append(twitter)
            # any(i in b for i in a)
            # for palavra in texto:
            #     if palavra in adverbios_negacao:
            #         twitters_negativos.append(twitter)
            #         break
            #     elif palavra in substantivos_negativos:
            #         twitters_negativos.append(twitter)
            #         break
            #     elif palavra in adverbios_positivos:
            #         twitter_positivos.append(twitter)
            #         break
            #     else:
            #         twitters_neutros.append(twitter)
            #         break

        return [twitters_negativos, twitter_positivos, twitters_neutros]