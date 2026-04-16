import random

temp = [random.randint(50, 100) for _ in range(20)]

for t in temp:
    print(t, "°C")
    if t > 80:
        print("Alerta: Temperatura elevada!")
        