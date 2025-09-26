# Schrijf een programma dat de gebruiker vraagt om zijn uurloon,
# het aantal uur dat hij of zij gewerkt heeft en dat daarna het salaris uitprint.


uurloon = input("Wat is je uurloon?")
uren = input("Hoeveel uur heb je gewerkt:")
uurloon =float(uurloon)
uren= float(uren)
salaris = ( uurloon * uren )
print(f"Je hebt {salaris} verdient.")
