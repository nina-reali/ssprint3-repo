import configparser
import csv
import boto3
import tweepy as tw
import pandas as pd
from datetime import date, time, datetime, timedelta
from botocore.exceptions import NoCredentialsError
import os
import pathlib
my_api_key = "lpbZJ29uL0oC6Uty7zy3zH5m9"
my_api_secret = "viamWQnB6LEClTuxTc5Mq1AzmJW7m2hNo2M4wwnG4eMJ0bLCyN"
my_bearer = "AAAAAAAAAAAAAAAAAAAAAHQncwEAAAAAoiFuCkN2Ah3prsmiczwgaEpZZf0%3DqqTgWWvdvVtMcfA2w8HUAgAhBgafyS1kdN1xOMVwc1RIs8Xwwx"
# authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True,timeout=200)


search_query = ["#nubank -filter:retweets","#c6 -filter:retweets","#inter -filter:retweets","#safra -filter:retweets","#santander -filter:retweets","#pix -filter:retweets"]


tweets_copy = []
header = ['id','nome', 'data', 'texto']
file = 'twiter.csv'
with open(file, 'w', encoding='UTF8') as f:
    writer = csv.writer(f,quoting=csv.QUOTE_NONNUMERIC, delimiter=";")
    writer.writerow(header)
    for query in search_query:
        tweets = tw.Cursor(api.search_tweets,
              q=query,
              lang="pt").items(1000)

        for tweet in tweets:
            texto=str(tweet.text).rstrip('\n')
            texto=texto.rstrip('\n')
            texto=texto.rstrip('\t')
            texto=texto.rstrip('\r')
            texto=texto.replace("\n","")
            linha= [tweet.id,str(tweet.user.name).rstrip('\n').replace('"',""),str(tweet.created_at).rstrip('\n'),texto]
            writer.writerow(linha)
       
    
    




def upload_to_aws(bucket, arquivo):
    s3 = boto3.client('s3')
    bucket=bucket
    local_file = os.path.join(pathlib.Path(__file__).parent.resolve(), arquivo)

    try:
        s3.upload_file(local_file, bucket, arquivo)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False

uploaded = upload_to_aws(bucket="config-spark-sptech-bucket-bruto", arquivo="twiter.csv")


