money = int(input("Pul kiriting: "))
length = float(input("Masofani km da kiriting: "))
taxi_price = int(input("Taxi narxini kiriting: "))
bus_price = int(input("Avtobus narxini kiriting: "))
bus_num = int(input("Nechta avtobusligini kiriting: "))

bus_main = (bus_price * bus_num)
bus_money = bus_main <= money

Taxi_main = length * taxi_price
taxi_money = Taxi_main <= money

print(f"Avtobus umumiy narxi {bus_price} * {bus_num} = {bus_main}: {bus_money}\nTaxi umumiy narxi {length} * {taxi_price} = {Taxi_main}: {taxi_money}")

if (bus_money == True and taxi_money == True):
    print("Sen ikkalasida ham keta olasan")
    if(taxi_money <= money):
        print("Sen taxida ketasan")
elif (bus_money <= money):
    print("Sen avtobusda ketasan")
