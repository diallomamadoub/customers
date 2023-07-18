#Extraction des données commentaires sur le site 

import pandas as pd
import time
import requests
from bs4 import BeautifulSoup

base_url = "https://fr.trustpilot.com/review/hellofresh.fr?page={}"
liste_page = [base_url.format(page_num) for page_num in range(1, 575)]

df_com = pd.DataFrame(columns=["auteur", "opinion", "commentaire", "note", "date"])

for url_Restaurants_Bars in liste_page:
    # Ajouter un délai d'attente de 2 secondes entre chaque requête
    time.sleep(2)

    # Début du scraping pour la page sélectionnée en utilisant requests
    response = requests.get(url_Restaurants_Bars)

    # Vérifier si la requête a réussi (code 200)
    if response.status_code == 200:
        bs_Restaurants_Bars = BeautifulSoup(response.content, 'html.parser')

        # Extraction des informations des avis
        commentaire = bs_Restaurants_Bars.findAll('p', attrs={'class': 'typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn'})
        auteur = bs_Restaurants_Bars.findAll('span', attrs={'class': 'typography_heading-xxs__QKBS8 typography_appearance-default__AAY17'})
        date_com = bs_Restaurants_Bars.findAll('p', attrs={'class': 'typography_body-m__xgxZ_ typography_appearance-default__AAY17'})
        com_gen = bs_Restaurants_Bars.findAll('h2', attrs={'class': 'typography_heading-s__f7029 typography_appearance-default__AAY17'})
        note = bs_Restaurants_Bars.findAll('div', attrs={'class': 'star-rating_starRating__4rrcf star-rating_medium__iN6Ty'})

        com = []
        for i in commentaire:
            com.append(i.text)
        aut = []
        for i in auteur:
            aut.append(i.text)
        com_g = []
        for i in com_gen:
            com_g.append(i.text)
        nott = []
        for i in note:
            alt_text = i.find('img')['alt']
            split_text = alt_text.split()
            if len(split_text) >= 2:
                nott.append(split_text[1])
            else:
                nott.append(None)

        dat_c = []
        for i in date_com:
            dat_c.append(i.text.replace("Date de l'expérience:", ""))

        df_temp = pd.DataFrame(list(zip(aut, com_g, com, nott, dat_c)), columns=["auteur", "opinion", "commentaire", "note", "date"])
        df_com = pd.concat([df_com, df_temp], ignore_index=True)
    else:
        print(f"Erreur lors de la récupération de la page {url_Restaurants_Bars}")

# Enregistrement du DataFrame dans un fichier CSV avec le séparateur ";"
output_file = 'verbatims.csv'
df_com.to_csv(output_file, sep=';', index=False)

print(f"Le DataFrame a été enregistré dans le fichier CSV : {output_file}")

