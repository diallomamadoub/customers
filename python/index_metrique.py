from elasticsearch import Elasticsearch

# Connexion à Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])  # Remplacez localhost et 9200 par les informations de connexion à votre cluster Elasticsearch

# Nom de l'index Elasticsearch
index_name = 'restaurant_reviews'

# Supprimer l'index s'il existe déjà
if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)

# Mapping Elasticsearch
mapping = {
    'properties': {
        'variety': {'type': 'integer'},
        'display': {'type': 'integer'},
        'price': {'type': 'integer'},
        'service': {'type': 'integer'},
        'decor': {'type': 'integer'},
        'time': {'type': 'integer'},
        'cleanliness': {'type': 'integer'},
        'flavor': {'type': 'integer'},
        'quantity': {'type': 'integer'}
    }
}

# Créer l'index avec le mapping spécifié
es.indices.create(index=index_name, body={'mappings': mapping})

print("Index créé avec succès !")


