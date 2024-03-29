# customers

===========LISEZ ATTENTIVEMENT CE DOCUMENT==================
Notre projet consiste à analyser la satisfaction client à partir des ressentis client via le site internet ( des verbatims).
Nous avons d'abord choisi une entreprise qui travaille dans le domaine de restauration. 
Ensuite nous avons choisi une liste des métriques:

*Variété du menu(variety)* : Mesurez la satisfaction des clients concernant la variété des plats proposés dans le menu. Les commentaires peuvent inclure des remarques sur la diversité des options disponibles.

*Présentation des plats(display)* : Évaluez la satisfaction des clients concernant la présentation visuelle des plats. Les commentaires peuvent inclure des remarques sur l'esthétique et l'attrait des plats.

*Prix(price)* : Mesurez la satisfaction des clients concernant les prix des plats proposés. Les commentaires peuvent inclure des remarques sur la valeur perçue par rapport aux prix.

*Service client(service)* : Évaluez la satisfaction des clients concernant le service fourni par le personnel du restaurant. Les commentaires peuvent inclure des remarques sur la courtoisie, l'efficacité et l'attention du personnel.

*Ambiance et décoration(decor)* : Mesurez la satisfaction des clients concernant l'ambiance générale et la décoration du restaurant. Les commentaires peuvent inclure des remarques sur l'atmosphère et le confort du lieu.

*Temps d'attente(time)* : Évaluez la satisfaction des clients concernant le temps d'attente pour être servi. Les commentaires peuvent inclure des remarques sur la rapidité du service.

*Propreté(cleanliness)* : Mesurez la satisfaction des clients concernant la propreté du restaurant. Les commentaires peuvent inclure des remarques sur la propreté des tables, des couverts, etc.

*Goût et saveur(flavor)* : Évaluez la satisfaction des clients concernant le goût et la saveur des plats. Les commentaires peuvent inclure des remarques sur le goût authentique des plats.

*Portions(quantity* : Mesurez la satisfaction des clients concernant la taille des portions des plats servis. Les commentaires peuvent inclure des remarques sur la quantité de nourriture par rapport au prix.

1) pour exporter en fichier CSV l'ensemble des commentaires (verbatims) il faut exécuter le programme python

python3 python/webscrapping.py

2) pour créér l'index il faut exécuter le programme python suivant:
python3  python/index.py

# Decription du code index.py

index.py est un code python qui:
1)Charge des données à partir d’un fichier CSV nommé 'verbatims.csv' dans un DataFrame pandas.
2)Convertit les dates au format texte en dates au format ISO.
3)Se connecte à Elasticsearch sur localhost:9200.
4)Supprime l’index Elasticsearch s’il existe déjà.
5)Ajoute des champs avec des valeurs par défaut de 0 au DataFrame pandas.
6)Crée un index Elasticsearch nommé 'hellofresh_reviews' avec un mapping spécifié.
7)Convertit la colonne 'note' en nombres flottants.
8)Importe les données du DataFrame dans Elasticsearch en tant que documents.
