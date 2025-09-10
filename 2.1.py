#1,0 = 30 euro
#2,5 = 75 euro
#10 =  300 euro

# Ik denk dat ik voor cijferPROJA een 8 ga halen.
# Ik denk dat ik voor cijferPROG een 7,5 ga halen.
# Ik denk dat ik voor cijferMOD een 8,5 ga halen.

cijferPROJA= 8
cijferPROG = 7.5
cijferMOD = 8.5

gemiddelde = (cijferPROJA + cijferPROG + cijferMOD ) / 3
print(gemiddelde)

beloning = (cijferPROJA + cijferPROG + cijferMOD) * 30


overzicht = f"Mijn cijfers zijn gemiddeld een {gemiddelde:.1f}, en ik verdien {beloning:.1f} euro."
print(overzicht)