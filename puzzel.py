# # Opdracht
# Onderstaande code is een puzzel.
# De 7 coordinaten vormen een woord van 7 letters.
# Ontcijfer elk coordinaat een voor een tot een letter uit de puzzel lijst.
# Sla jou ontcijferde letters op in de “antwoord” variabele
# Print je antwoord uit.

puzzel = ["Albatros", "poncho", "vlinder", "glitter", ]
coordinaten = [(0,0),(2,0),(0,-2),(1,3),(0,3),(2,4),(1,-1)]

antwoord = puzzel[0][0] + puzzel[2][0] + puzzel[0][-2] + puzzel[1][3] + puzzel[0][3] + puzzel[2][4] + puzzel[1][-1]

print(antwoord)

# Alternetieve uitwerking

antwoord_lijst = []

antwoord_lijst.append(puzzel[coordinaten[0][0]][coordinaten[0][1]])
antwoord_lijst.append(puzzel[coordinaten[1][0]][coordinaten[1][1]])
antwoord_lijst.append(puzzel[coordinaten[2][0]][coordinaten[2][1]])
antwoord_lijst.append(puzzel[coordinaten[3][0]][coordinaten[3][1]])
antwoord_lijst.append(puzzel[coordinaten[4][0]][coordinaten[4][1]])
antwoord_lijst.append(puzzel[coordinaten[5][0]][coordinaten[5][1]])
antwoord_lijst.append(puzzel[coordinaten[6][0]][coordinaten[6][1]])

print(antwoord_lijst)

# Nog alternatieve uitwerking gebruiken for loop

antwoord = []

for coordinaat in coordinaten:
    antwoord.append(puzzel[coordinaat[0]][coordinaat[1]])

print(antwoord)    

# Nog andere  for x,y loop (twee variabelen)

antwoord = []

for x,y in coordinaten:
    antwoord.append(puzzel[x][y])

print(antwoord)

# in a string

antwoord = ""

for x,y in coordinaten:
    antwoord += puzzel[x][y]

print(antwoord)    

# changing a list of letters to a string

antwoord = []

for x,y in coordinaten:
    antwoord.append(puzzel[x][y])

print("".join(antwoord))



