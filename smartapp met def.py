# Eerst vraag ik informatie op om mijn variabelen aan te vullen
def infodag(dag):
    celcius_input = input(f"Wat is op dag {dag} de temperatuur in graden Celsius? ")
    if celcius_input == "":
        print("bye")
        return None, None, None
    celcius = float(celcius_input)

    windsnelheid_input = input(f"Wat is op dag {dag} de windsnelheid in meter per seconde? ")
    if windsnelheid_input == "":
        print("bye")
        return None, None, None
    windsnelheid = float(windsnelheid_input)

    vocht_input = input(f"Wat is op dag {dag} de luchtvochtigheid als percentage (0–100)? ")
    if vocht_input == "":
        print("bye")
        return None, None, None
    luchtvochtigheid = int(vocht_input)

    return celcius, windsnelheid, luchtvochtigheid

#Aangezien ik nu celcius, windsnelheid en luchtvochtigheid weet kan ik  het gevoelstemperatuur berekenen en het temperatuur in fahrenheit
def bereken_temperaturen(celcius, windsnelheid, luchtvochtigheid):
    temperatuur_fahrenheit = celcius * 1.8 + 32
    gevoelstemperatuur = celcius - (luchtvochtigheid / 100) * windsnelheid
    return temperatuur_fahrenheit, gevoelstemperatuur

# Nu geef ik advies aan de gebruiker doormiddel van het gevoelstemperatuur en het windsnelheid

def advies(gevoelstemperatuur, windsnelheid):
    if gevoelstemperatuur < 0 and windsnelheid > 10:
        print("Het is heel koud en het stormt! Verwarming helemaal aan!")
    elif gevoelstemperatuur < 0 and windsnelheid <= 10:
        print("Het is behoorlijk koud! Verwarming aan op de benedenverdieping!")
    elif 0 <= gevoelstemperatuur < 10 and windsnelheid > 12:
        print("Het is best koud en het waait; verwarming aan en roosters dicht!")
    elif 0 <= gevoelstemperatuur < 10 and windsnelheid <= 12:
        print("Het is een beetje koud, elektrische kachel op de benedenverdieping aan!")
    elif 10 <= gevoelstemperatuur < 22:
        print("Heerlijk weer, niet te koud of te warm.")
    else:
        print("Warm! Airco aan!")

def bereken_gemiddelde(temperaturen):
    return sum(temperaturen) / len(temperaturen)

# Aangezien je informatie moet opvragen voor 7 dagen maak ik een loop lijst
dagen = []
alle_dagen = 7


#ik heb voor (1, alle_dagen +1) chat gpt gebruik want ik snapte niet waarom die begon met dag 0, maar dat komt omdat een
#lijst begint bij 0, voor de rest heb ik de rest wel zelf gemaakt alleen het stukje (1, alle_dagen +1)
for dag in range(1, alle_dagen + 1):
    celcius, windsnelheid, luchtvochtigheid = infodag(dag)
    if celcius is None:
        break
# Ik heb voor .1f gebruik gemaakt van chatgpt want ik wist niet hoe ik dat moest doen.
    temperatuur_fahrenheit, gevoelstemperatuur = bereken_temperaturen(celcius, windsnelheid, luchtvochtigheid)
    print(f"De temperatuur in Fahrenheit is {temperatuur_fahrenheit:.1f}")
    print(f"De gevoelstemperatuur is {gevoelstemperatuur:.1f}")

    advies(gevoelstemperatuur, windsnelheid)

    dagen.append(celcius)
    gemiddelde = bereken_gemiddelde(dagen)
    print(f"Het gemiddelde temperatuur tot nu toe is {gemiddelde:.1f}")
    print("=" * 38)
