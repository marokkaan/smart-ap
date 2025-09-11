celcius = float(input("Wat is de temperatuur in graden celcius?"))
windsnelheid = float(input("Wat is het windsnelheid in meter per seconde?"))
luchtvochtigheid= int(input("Wat is de luchtvochtigheid als geheel percentage 0-100"))

temperatuur_fahrenheit = celcius * 1.8 + (32)

print (f"De temperatuur in fahrenheit is {temperatuur_fahrenheit}")

gevoelstemperatuur = celcius - luchtvochtigheid / 100 * windsnelheid

print (f"Het gevoelstemperatuur is {gevoelstemperatuur}")

if gevoelstemperatuur < 0 and windsnelheid > 10:
        return ("Het is heel koud en het stormt! Verwarming helemaal aan!")
    elif gevoelstemperatuur < 0 and windsnelheid <= 10:
        return ("Het is behoorlijk koud! Verwarming aan op de benedenverdieping!")
    elif 0 <= gevoelstemperatuur < 10 and windsnelheid > 12:
        return ("Het is best koud en het waait; verwarming aan en roosters dicht!")
    elif 0 <= gevoelstemperatuur < 10 and windsnelheid <= 12:
        return ("Het is een beetje koud, elektrische kachel op de benedenverdieping aan!")
    elif 10 <= gevoelstemperatuur < 22:
        return ("Heerlijk weer, niet te koud of te warm.")
    else:
        return ("Warm! Airco aan!")

