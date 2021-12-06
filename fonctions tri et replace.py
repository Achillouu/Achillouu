def tri(b):
    """cherche une lettre dans un mot.
cherche une lettre dans un mot donnés en argument.
Parameters
----------
a : str
lettre à chercher
b : str
mot à chercher
Returns
-------
int
une lettre dans un mot
"""
    a=input("Donnez UNE lettre : ")
    g=[]
    if a in b:
        for i in range(len(b)):
            if a==b[i]:
                g.append(i)
    else: 
        g.append(99)
    return g

#tri(a,b)=ListeTrouve
#ListeNonTrouve=["_","_","_","_","_","_","_"]
#mot="oiseaux"

def replace(ListeTrouve,ListeNonTrouve,mot):
    """Incrémente une valeur donnée à une position donnée à une liste d'inconnues.
Parameters
----------
ListeTrouve : liste str
 Liste des positions des inconnues à changer en lettre
ListeNonTrouve : Liste str
 Liste des inconnues et lettres déjà trouvées
mot : str
 référence des valeurs à incrémenter dans la liste d'inconnues
-------
int
une lettre dans un mot
"""
    for i in ListeTrouve:
        ListeNonTrouve[i]=mot[i]
    return ListeNonTrouve
        
    