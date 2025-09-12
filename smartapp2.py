dagen = []
alle_dagen = 7

for dag in range(1, alle_dagen + 1):
    celcius_input = input(f"Wat is op dag {dag} de temperatuur in graden Celsius? ")
    if celcius_input == "":
        print("bye")
        break
    celcius = float(celcius_input)

    wind_input = input(f"Wat is op dag {dag} de windsnelheid in meter per seconde? ")
    if wind_input == "":
        print("bye")
        break
    windsnelheid = float(wind_input)

    vocht_input = input(f"Wat is op dag {dag} de luchtvochtigheid als percentage (0–100)? ")
    if vocht_input == "":
        print("bye")
        break
    luchtvochtigheid = int(vocht_input)


    temperatuur_fahrenheit = celcius * 1.8 + 32
    print(f"De temperatuur in Fahrenheit is {temperatuur_fahrenheit:.1f}")

    gevoelstemperatuur = celcius - (luchtvochtigheid / 100) * windsnelheid
    print(f"De gevoelstemperatuur is {gevoelstemperatuur:.1f}")


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


    dagen.append(celcius)
    gemiddelde = sum(dagen) / len(dagen)
    print(f"Het gemiddelde temperatuur tot nu toe is {gemiddelde:.1f}")
    print("=" * 38)
