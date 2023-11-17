age = 48

if age >= 18:
    print("mayor de edad")
else:
    print("menor de edad")

price = 500
has_card = True

if has_card:
    print(price-100)
elif price < 100:
    print(price-50)
else:
    print(price-10)

#Lista en Python = Array en JS
colors = ["Yellow","Red","Brown","Black","White"]
print("=== FOR IN ===")
#for (let i = 0; i <= colors.lenght; i++) JAVASCRIPT
#for (let variable of array)

for color in colors:
    print(color)

#Lista dentro de una lista
teams = [
    "Barcelona", 
    "Real Madrid",
    "PSG","Boca Jr",  
    ["Messi", "CR7","Mbape","Pepe"]]

players = teams[4]

for player in players:
    print(player)

print("===RANGE===")
numbers = range(101)  #retorna variable tipo range
print(list(numbers))

numbers2 = range(12,21)
print(list(numbers2))

numbers3 = range(20,101,5)
print(list(numbers3))

for number in range(1,10):
    if number % 2 == 0:
        print(f"{number} es par")
    else:
        print(f"{number} es impar")
        