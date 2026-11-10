# main.py : programme principal de la playlist de party


# TODO 0 : corriger les erreurs de syntaxe dans le fichier playlist

# TODO 1 : importer le module playlist
from playlist import *

# TODO 2 : créer le dictionnaire vide ma_playlist
#          et les listes titres et durees (5 éléments chacune)
ma_playlist= {}
titres =("november rain","Wish you were here","comfortably numb","come out and play","easy lover")
duree = (       530,           300,                   250,             150,             200      )

# TODO 3 : avec une boucle for et range(len(titres)),
#          ajouter chaque chanson à ma_playlist, en utilisant le module
for i in range(len(titres)):
    ajouter_chanson(ma_playlist,titres[i],duree[i])

# TODO 4 : afficher chaque chanson avec sa durée formatée
#          (ex. : Nuit blanche - 3:05)
for i in range(len(titres)):
    chanson = titres[i]
    duree_secondes = duree[i]
    total = (chanson) + "-" + " " +  formater_duree(duree_secondes)
    print (total)

# TODO 5 : afficher la durée totale de la playlist, formatée
duree_totale_secondes = sum(duree)

# On passe le total des secondes à votre fonction de formatage
duree_formatee = formater_duree(duree_totale_secondes)

print("Durée totale de la playlist :", duree_formatee)

# todo 6 afficher la chanson la plus longue
print("chanson la plus longue:" , chanson_la_plus_longue(ma_playlist))

# TODO 7 : demander une durée maximale en secondes (input, converti en int),
#          puis afficher la liste des chansons plus courtes que cette durée
try:
    duree = input("quelle est la duree maximale en secondes ? :")
    liste_chansons_courtes = chansons_courtes(ma_playlist, duree)
    print(liste_chansons_courtes)
except:
    print("erreur la duree doit etre un entier")
# TODO 8 : demander le titre d'une chanson à retirer
#          - si elle est absente : afficher un message
#          - sinon : la retirer et réafficher la playlist

titre = input ("entrer le titre a retirer: ")
if not titre in ma_playlist :
    print("cette chanson neest pas dans ma playlist")
else:
    ma_playlist = retirer_chanson(ma_playlist,titre)
    print (ma_playlist)



# TODO 9 : tester votre programme, corriger les erreurs d'exécutions et de logique
#          incluant celles dans le module.

# TODO 10 : tester avec des valeurs incorrectes, exemple un titre qui n'existe pas,
#           une durée en str, et ajouter la gestion d'exceptions, incluant dans le module.