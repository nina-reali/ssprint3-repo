import configparser
import csv
import boto3
import re
from service_tratar_tweeter import ServiceTratarTweeter
from credentials_twitter import CredentialsTwitter
from get_twitters import GetTwitters
from collections import namedtuple
from analyzer import Analyzer
from service_writer_json import WriterJson

# search_query = ["#nubank -filter:retweets","#c6 -filter:retweets","#inter -filter:retweets","#safra -filter:retweets","#santander -filter:retweets","#pix -filter:retweets"]
# get_twitters = GetTwitters().get(search_query)

# tweets_copy = []
# header = ['id','nome', 'data', 'texto']
file = '../twiter.csv'


# def remover_url_from_text(texto):
#     return re.sub(r'http\S+', '', texto)

# with open(file, 'w', encoding='UTF8') as f:
#     writer = csv.writer(f,quoting=csv.QUOTE_NONNUMERIC, delimiter=";")
#     writer.writerow(header)

#     for query in search_query:
#         tweets = tw.Cursor(api.search_tweets,
#               q=query,
#               lang="pt").items(1000)

#         for tweet in tweets:
#             if 'pix' in tweet.text:
#                 texto = ServiceTratarTweeter(tweet.text).remover_quebra_de_linhas()
#                 texto = remover_url_from_text(texto)
#                 linha= [tweet.id,str(tweet.user.name).rstrip('\n').replace('"',""),str(tweet.created_at).rstrip('\n'),texto]
#                 writer.writerow(linha)

twitter_named_tuple = namedtuple("Twitter", ["id", "nome", "data", "texto"])
import csv

twitters = []

with open(file, mode='r') as file:

    csvFile = csv.reader(file)
    next(csvFile)

    for lines in csvFile:
        linha = lines[0]
        linha = linha.split(";")
        twitters.append(twitter_named_tuple(linha[0], linha[1], linha[2], linha[3]))

tratar_tweeter = ServiceTratarTweeter(twitters)
twitters = tratar_tweeter.remover_quebra_de_linhas()
analyzer = Analyzer(twitters)
tweets_negativos, tweeets_positivos, tweets_neutros = analyzer.filtrar_tweets()

twitters = []
for tweet in tweets_negativos:
    twitters.append({'sentimento': 0, 'tweet': tweet._asdict()})

for tweet in tweeets_positivos:
    twitters.append({'sentimento': 2, 'tweet': tweet._asdict()})

for tweet in tweets_neutros:
    twitters.append({'sentimento': 1, 'tweet': tweet._asdict()})

write_json = WriterJson(twitters)
write_json.write()



# def upload_to_aws(bucket, arquivo):
#     s3 = boto3.client('s3')
#     bucket=bucket
#     local_file = os.path.join(pathlib.Path(__file__).parent.resolve(), arquivo)

#     try:
#         s3.upload_file(local_file, bucket, arquivo)
#         print("Upload Successful")
#         return True
#     except FileNotFoundError:
#         print("The file was not found")
#         return False

# uploaded = upload_to_aws(bucket="config-spark-sptech-bucket-bruto", arquivo="twiter.csv")


