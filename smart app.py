celcius = float(input("Wat is de temperatuur in graden celcius?"))
windsnelheid = float(input("Wat is het windsnelheid in meter per seconde?"))
luchtvochtigheid= int(input("Wat is de luchtvochtigheid als geheel percentage 0-100"))

temperatuur_fahrenheit = celcius * 1.8 + (32)

print (f"De temperatuur in fahrenheit is {temperatuur_fahrenheit}")

gevoelstemperatuur = celcius - luchtvochtigheid / 100 * windsnelheid

print (f"Het gevoelstemperatuur is {gevoelstemperatuur}")
