maand = int(input("Geef een maandnummer en ik zeg welk seizoen dat is."))
if maand in  ( 1, 12 , 2) :print ("Het is winter")
elif maand in (9, 10 , 11): print ("Het is herfst")
elif maand in  (6, 7, 8): print ("Het is zomer")
elif maand in (3, 4, 5): print("Het is lente")

else:
    print ("Geef een geldig maandnummer op, dus tussen 1 en 2")




# 1 - Lente: Maart (3), April (4), Mei (5)
# Zomer: Juni (6), Juli (7), Augustus (8)
# Herfst: September (9), Oktober (10), November (11)
# Winter: December (12), Januari (1), Februari (2)

