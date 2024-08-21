#      set les input de question 
q1 = input("Quel est ton Rang ? : ")
q2 = int(input("Combien de RR ? : "))

#       set up de variables
rank = q1 + " " + str(q2) + " RR"
maxRR = 100

#       set up de condition
if maxRR - q2 < 50:
    avantrankup = str(maxRR - q2) + str(" RR avant de rank up ! T'es fort en vrai tu va bientôt monter")
elif maxRR - q2 >= 50:
    avantrankup =  str(maxRR - q2) + str(" RR avant de rank up ! Tu mérite pas ton rang BOZO")

#       set up de l'affichage
print("=======================")
print("Tu es " + rank)
print("Il te manque " + str(avantrankup))
print("=======================")
