import random

dados = [random.randint(0, 100) for _ in range(100)]

criticos = [d for d in dados if d > 80]

print("Dados críticos:", criticos)