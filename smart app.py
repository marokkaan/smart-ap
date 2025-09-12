celcius = float(input("Wat is de temperatuur in graden Celsius? "))
windsnelheid = float(input("Wat is de windsnelheid in meter per seconde? "))
luchtvochtigheid = int(input("Wat is de luchtvochtigheid als geheel percentage (0–100)? "))


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
