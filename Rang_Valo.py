import os
maxRR = 100

#       set up de l'affichage
os.system("cls")
print("Quel est ton rang ?")
print("1- Iron")
print("2- Bronze")
print("3- Silver")
print("4- Gold")
print("5- Platine")
print("6- Diamant")
print("7- Ascendant")
print("8- Immortal")
print("9- Radiant")
reponse = int(input("Entrez votre réponse et appuyez sur Entrée (Enter) : "))
rank = reponse



"""if rank == "1":
   reponse = "Iron"

elif rank == "2":
   reponse = "Bronze"

elif rank == "3":
   reponse = "Silver"

elif rank == "4":
   reponse = "Gold"

elif rank == "5":
   reponse = "Platine"

elif rank == "6":
   reponse = "Diamant"

elif rank == "7":
   reponse = "Ascendant"

elif rank == "8":
   reponse = "Immortal"

elif rank == "9":
   reponse = "Radiant"

rank, reponse = reponse, rank """




if reponse == 1:

    q2 = int((input("Iron 1, 2 ou 3 ? : ")))
    if q2 >= 1 and q2 <= 3:
       currentRR = int(input("Combiens de RR ? : "))
       if currentRR >= 0 and currentRR <= 99 :
         print("=======================")
         print("Tu es Iron " + str(q2) + " avec " + str(currentRR) + " RR")
         print("Il te manque " + str(maxRR - currentRR) + " RR avant de rank up !")
         print("=======================")
    
if reponse == 2:

    q2 = int((input("Bronze 1, 2 ou 3 ? : ")))
    if q2 >= 1 and q2 <= 3:
       currentRR = int(input("Combiens de RR ? : "))
       if currentRR >= 0 and currentRR <= 99 :
         print("=======================")
         print("Tu es Bronze " + str(q2) + " avec " + str(currentRR) + " RR")
         print("Il te manque " + str(maxRR - currentRR) + " RR avant de rank up !")
         print("=======================")

if reponse == 3:

    q2 = int((input("Silver 1, 2 ou 3 ? : ")))
    if q2 >= 1 and q2 <= 3:
       currentRR = int(input("Combiens de RR ? : "))
       if currentRR >= 0 and currentRR <= 99 :
         print("=======================")
         print("Tu es Silver " + str(q2) + " avec " + str(currentRR) + " RR")
         print("Il te manque " + str(maxRR - currentRR) + " RR avant de rank up !")
         print("=======================")
        
if reponse == 4:

    q2 = int((input("Gold 1, 2 ou 3 ? : ")))
    if q2 >= 1 and q2 <= 3:
       currentRR = int(input("Combiens de RR ? : "))
       if currentRR >= 0 and currentRR <= 99 :
         print("=======================")
         print("Tu es Gold " + str(q2) + " avec " + str(currentRR) + " RR")
         print("Il te manque " + str(maxRR - currentRR) + " RR avant de rank up ")
        # Ligne dessous en commentaire parce que j'essaye de donné le Next rank 
        # print("Ton prochain rang est : " + str(rank + 1))
         print("=======================")
    
if reponse == 5:

    q2 = int((input("Platine 1, 2 ou 3 ? : ")))
    if q2 >= 1 and q2 <= 3:
       currentRR = int(input("Combiens de RR ? : "))
       if currentRR >= 0 and currentRR <= 99 :
         print("=======================")
         print("Tu es Platine " + str(q2) + " avec " + str(currentRR) + " RR")
         print("Il te manque " + str(maxRR - currentRR) + " RR avant de rank up !")
         print("=======================")

if reponse == 6:

    q2 = int((input("Diamant 1, 2 ou 3 ? : ")))
    if q2 >= 1 and q2 <= 3:
       currentRR = int(input("Combiens de RR ? : "))
       if currentRR >= 0 and currentRR <= 99 :
         print("=======================")
         print("Tu es Diamant " + str(q2) + " avec " + str(currentRR) + " RR")
         print("Il te manque " + str(maxRR - currentRR) + " RR avant de rank up !")
         print("=======================")
        
if reponse == 7:

    q2 = int((input("Ascendant 1, 2 ou 3 ? : ")))
    if q2 >= 1 and q2 <= 3:
       currentRR = int(input("Combiens de RR ? : "))
       if currentRR >= 0 and currentRR <= 99 :
         print("=======================")
         print("Tu es Ascendant " + str(q2) + " avec " + str(currentRR) + " RR")
         print("Il te manque " + str(maxRR - currentRR) + " RR avant de rank up !")
         print("=======================")
        
if reponse == 8:

    q2 = int((input("Immortal 1, 2 ou 3 ? : ")))
    if q2 >= 1 and q2 <= 3:
       currentRR = int(input("Combiens de RR ? : "))
       if currentRR >= 0 and currentRR <= 99 :
         print("=======================")
         print("Tu es Immortal " + str(q2) + " avec " + str(currentRR) + " RR")
         print("Il te manque " + str(maxRR - currentRR) + " RR avant de rank up !")
         print("=======================")
        
if reponse == 9:

    q2 = "Radiant"
    currentRR = int(input("Combiens de RR ? : "))
    if currentRR >= 0 :
     print("=======================")
     print("Tu es Radiant"  + " avec " + str(currentRR) + " RR")
     print("Tu as atteint le Rang maximum, Félicitation")
     print("=======================")