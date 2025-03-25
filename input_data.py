from model.repas import *


print('Bienvenue dans le programme de gestion de repas')
repas =' '
while repas != '':
    repas = input('Ajouter un repas ')

    if repas!= '':
        name = input('nom repas : ')
        prix = input('prix repas : ')
        type = input('type repas : ')
        photo = f"{name.lower()}.jpg"
        r = Repas(name, photo, prix, type)
        r.Add_Repas()
        composant = ' '
        composants = []
        while composant != '':
            composant = input('nom composant : ')
            if composant!= '':
                composants.append(composant)
                c = Composant(composant)
                if c.Search() == False:
                    c.Add()
                
                cr = ComposantRepas(r.Get_id(), c.Get_id())
                if cr.Search() == False:
                    cr.Add()
        print(composants)
    # ajouter au panier