#Chuiffrement

text = 'bonjour le monde' #Ici le texte que nous voulons chiffré 
key = 4 #Ici la clé qui nous permet d'effectuer le chiffrement
chiffre = "" #Ici une chaine de caractere qui nous permet de collecter chaque lettre chiffré

for lettre in text :          #Boucle nous permettant d'effectuer le parcours sur le texte 
    if not ord(lettre) == 32:  #Ici c'est la verication si lettre n'est pas un caractere vide 
        val_lettre = ord(lettre) - 97   #Converssion de la lette en Int 
        temp = (val_lettre + key)%26     #Ici s'effectue le chiffrement du Int en caractere compris entre A et Z
        lettre = chr(temp + 97)             #Transformation en Int
chiffre += lettre                       #Ajout de la valeur au texte
    

print(chiffre)