"""
fruits_basket = ["fruit1", "fruit2", "fruit3", "fruit4"]

print("Your fruits in the basket: ")

for i in range(len(fruits_basket)):
    print(f"{i + 1}. {fruits_basket[i]}")

print()

while True:

    user = input("How many fruits would you like to catch?: ")
    break
    
    fruits_basket.append(user)
print("Basket: ")

for i in range(len(fruits_basket)):
    print(f"{i + 1}. {fruits_basket[i]}")
"""

IsTrue = True
fruits_basket = []

while IsTrue:
    catch = int(input("How many would you like to catch?: "))


    for i in range(catch):
        print(i)
        while IsTrue:
            fruit = input("What fruit? (\"A\" for Apple, \"O\" for Orange, \"M\" for Mango, \"G\" for Guava): ")
            if i in (str(fruit)) == "A":
                
                fruits_basket.append("Apple")



    print("Fruits basket: ")

