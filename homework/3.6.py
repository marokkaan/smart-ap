string= "Guido van Rossum heeft programmeertaal Python bedacht."
for klinker in string:
    if klinker.lower() in "aeiou":
        print(klinker)