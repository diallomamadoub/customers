from elasticsearch import Elasticsearch
import pandas as pd
from datetime import datetime

# Charger les données du fichier CSV dans un DataFrame pandas
csv_file ='csv/verbatims.csv'
df_com = pd.read_csv(csv_file, sep=';')

print(df_com.head(5))

# Dictionnaire de correspondance des mois
correspondance_mois = {
    'janvier': '01', 'février': '02', 'mars': '03', 'avril': '04', 'mai': '05', 'juin': '06',
    'juillet': '07', 'août': '08', 'septembre': '09', 'octobre': '10', 'novembre': '11', 'décembre': '12'
}

def convertir_date_texte(date_texte):
    elements_date = date_texte.strip().split(' ')
    jour = elements_date[0]
    mois = correspondance_mois[elements_date[1].lower()]
    annee = elements_date[2]
    date_convertie = f'{annee}-{mois}-{jour}'
    return datetime.strptime(date_convertie, '%Y-%m-%d')
# ...

# Appliquer la fonction de conversion à la colonne "date"
df_com['date'] = df_com['date'].apply(convertir_date_texte)

print(df_com.head(5))

# Connexion à Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])  # Remplacez localhost et 9200 par les informations de connexion à votre cluster Elasticsearch

# Nom de l'index Elasticsearch
index_name = 'hellofresh_reviews'

# Supprimer l'index s'il existe déjà
if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)

# Mapping Elasticsearch
mapping = {
    'properties': {
        'auteur': {'type': 'keyword'},
        'opinion': {'type': 'text'},
        'commentaire': {'type': 'text'},
        'note': {'type': 'float'},
        'date': {'type': 'date'}
    }
}

# Créer l'index avec le mapping spécifié
es.indices.create(index=index_name, body={'mappings': mapping})


# Convertir la date au format ISO 8601 (par exemple, "2020-04-09T00:00:00Z")
#df_com['date'] = df_com['date'].apply(lambda x: parse(x, dayfirst=True).strftime('%Y-%m-%d'))
df_com['note'] = df_com['note'].str.replace(',', '.').astype(float)

# Importer les données dans Elasticsearch
for _, row in df_com.iterrows():
    doc = row.to_dict()
    es.index(index=index_name, body=doc)

print("Index créé avec succès !")

