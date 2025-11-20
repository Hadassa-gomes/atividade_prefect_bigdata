# load.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # carrega variáveis do .env

class Load:
    def __init__(self):
        # Conecta ao MongoDB Atlas usando a URI do .env
        self.client = MongoClient(os.getenv("MONGO_URI"))

    def load_data_atlas(self, data, db_name, collection_name):
        """
        Insere uma lista de dicionários 'data' na coleção especificada.
        """
        db = self.client[db_name]  # seleciona o banco
        collection = db[collection_name]  # seleciona a coleção
        if data:  # só insere se houver dados
            collection.insert_many(data)
            print(f"{len(data)} registros inseridos em {db_name}.{collection_name}")
        else:
            print("Nenhum dado para inserir.")



