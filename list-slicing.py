# # maak een boodschappenlijst
boodschappen = ['eiren', 'yoghurt', 'appels', 'uien', 'tomaten']
print(f"de eerste en de derede items zijn {boodschappen[0]} en {boodschappen[2]}")
x = boodschappen.pop()
print(boodschappen)
print(x)
boodschappen.pop()
print(boodschappen.reverse)


mijn_boodschappen = ['melk', 'eieren', 'kaas', 'koffie', 'gehakt', 'groente', 'fruit', 'kwark', 'kip', 'vis']
print(mijn_boodschappen[0:6:2])

numbers = [1, 2, 3, 4, 5, ]

# print middeste 3
print(numbers[1:4])

# eerste drie

print(numbers[:3])

# de tweede en de een na lateste
print(numbers[1:-1:2])

#achterstevoren
# numbers.reverse()

#achterstevoren andere manier zonder .reverse() method 
print(numbers[::-1])
