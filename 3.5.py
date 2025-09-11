#Schrijf een for-loop die over een lijst met getallen itereert, en alle even getallen print.
getallen = [1, 2, 3, 4, 5, 6, 7]
for getal in getallen:
    if getal % 2 == 0:
        print(getal)
