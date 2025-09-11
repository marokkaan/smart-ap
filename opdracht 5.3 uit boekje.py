# Vraag de gebruiker om drie getallen, en toon dan de grootste, de kleinste,
#en hun gemiddelde afgerond op twee decimalen.

getal1 = int(input("Geef me 3 getallen, geef me de eerste"))
getal2 = int(input("Geef me nu de tweede"))
getal3 = int(input("Geef me nu de derde"))
hoogste= (max(getal1, getal2, getal3))
laagste = (min(getal1, getal2, getal3))
gemiddelde = (getal1 + getal2 + getal3 ) / 3
print(f"Het gemiddelde is {gemiddelde}, het laagste getal is {laagste} en het hoogste is {hoogste}")



