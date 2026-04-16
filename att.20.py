import random

dados = [random.randint(0, 100) for _ in range(10)]

banco = []

for d in dados:
    print("Sensor:", d)

    if d > 80:
        print("CLP: Alerta!")
    
    banco.append(d)

print("Dados armazenados:", banco)

media = sum(banco)/len(banco)
print("Relatório - Média:", media)