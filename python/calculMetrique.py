from elasticsearch import Elasticsearch

# Connexion à Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Nom de l'index Elasticsearch
index_name = 'hellofresh_reviews'

# Requête pour récupérer tous les documents
query = {
    "query": {
        "match_all": {}
    }
}

# Exécution de la requête Elasticsearch pour récupérer tous les documents
result = es.search(index=index_name, body=query)

# Définition des termes positifs et négatifs pour chaque variable (à personnaliser)
positif_terms = {
    'quality': ['delicieux', 'savoureux', 'excellent', 'parfait', 'exceptionnel', 'gout'],
    'variety': ['diversifie', 'options variees', 'large choix', 'variety', 'diversity'],
    'display': ['bien presente', 'esthetique', 'plats joliment disposes', 'presentation', 'visuel'],
    'price': ['abordable', 'bon rapport qualite-prix', 'prix', 'valeur', 'economique'],
    'service': ['courtois', 'efficace', 'amical', 'service', 'personnel'],
    'decor': ['ambiance agreable', 'decor elegant', 'confortable', 'atmosphere', 'ambiance'],
    'time': ['service rapide', 'rapide', 'attente courte', 'rapidite'],
    'cleanliness': ['propre', 'tables propres', 'hygiene', 'nettoye', 'proprete'],
    'flavor': ['delicieux', 'savoureux', 'gout', 'saveur', 'parfum'],
    'quantity': ['portions genereuses', 'abondance de nourriture', 'quantite', 'portion', 'generosite']
}

negatif_terms = {
    'quality': ['mediocre', 'mauvais', 'mauvaise qualite', 'horrible', 'immonde', 'degoutant','il manqu'],
    'variety': ['monotone', 'peu de choix', 'manque de variete', 'repetitif'],
    'display': ['plats desordonnes', 'presentation negligee', 'aspect peu attrayant', 'repoussant'],
    'price': ['cher', 'couteux', 'trop cher', 'arnaque', 'expensif'],
    'service': ['lent', 'impoli', 'mauvais service', 'negligent', 'inefficace'],
    'decor': ['decor neglige', 'ambiance desagreable', 'inconfortable', 'vulgaire'],
    'time': ['longue attente', 'lenteur', 'service lent','attente jusqu', 'attente interminable'],
    'cleanliness': ['sale', 'couverts sales', 'hygiene douteuse', 'negligence', 'non propre'],
    'flavor': ['fade', 'insipide', 'sans saveur', 'gout fade', 'insatisfaisant'],
    'quantity': ['petites portions', 'insuffisant', 'trop peu', 'portion ridicule', 'penurie']
}

# Fonction pour évaluer les variables à partir des commentaires
def evaluer_variable(commentaire, positif_terms, negatif_terms):
    commentaire = commentaire.lower()
    score = 0
    for term in positif_terms:
        if term in commentaire:
            score += 1
    for term in negatif_terms:
        if term in commentaire:
            score -= 1
    return score

# Mettre à jour les documents dans l'index Elasticsearch avec les nouvelles valeurs
for hit in result['hits']['hits']:
    doc_id = hit['_id']
    source = hit['_source']
    for field in positif_terms.keys():
        score = evaluer_variable(source['commentaire'], positif_terms[field], negatif_terms[field])
        source[field] = score
    es.index(index=index_name, id=doc_id, body=source)

# Afficher les 20 premiers documents mis à jour
for hit in result['hits']['hits']:
    print(hit['_source'])

