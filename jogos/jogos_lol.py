import datetime as dtm
import os 
from dotenv import load_dotenv
import requests

load_dotenv()

class LolApi:

    def __init__(self):
        self.url = os.getenv("URL")
        self.token = os.getenv("TOKEN")
        self.header = { 
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Riot-Token": self.token
        } 

    def get_puuid(self, tagline, name):

        """Requisita dados da api para pegar o id do usuario

        ARGS:
            tagline(str): tag que identifica região onde o usuario está
            name(str): nome de usuario
        """ 

        self.inicio_coleta = self.registra_time('get_puuid')
        response = requests.get(url=f"{self.url}/riot/account/v1/accounts/by-riot-id/{name}/{tagline.upper()}", headers=self.header, verify=True)

        if response.status_code == 200:
            try:
                self.puuid_response = response.json()
                self.puuid = self.puuid_response.get('puuid')
                self.name = self.puuid_response.get('gameName')
                self.tagLine = self.puuid_response.get('tagLine')
                
                if self.puuid:
                    pass
                else:
                    print('Campo "puuid" não encontrado na resposta JSON.')
            except Exception as e:
                print(f'Erro ao processar resposta JSON: {e}')
        else:
            print(f'Erro na requisição. Código de status: {response.status_code}')

        return self.puuid
    
    def get_latest_games(self, limit = 10):
        """Requisita ids dos ultimos jogos

        ARGS:
            limit(int): quantidade de jogos retornados
        """ 

        ##self.inicio_coleta = self.registra_time('get_puuid')
        ##response = requests.get(url=f"{self.url}/lol/match/v5/matches/by-puuid/{self.puuid}/ids?count={limit}", headers=self.header, verify=True)
        ##return response.text


    def registra_time(self, etapa):
        time = dtm.datetime.now()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")
        log_entry = f"{timestamp} - Etapa: {etapa}\n"

        with open("log.txt", "a") as log_file:
            log_file.write(log_entry)

        return timestamp 

api = LolApi()
result = api.get_puuid('br1', 'gordovirje')
print(result)


