import random

limite = 500
consumos = [random.randint(300, 700) for _ in range(20)]

for c in consumos:
    print(c)
    if c > limite:
        print("Consumo ultrapassando os limites!")