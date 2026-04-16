import random

limite = 5
vibracoes = [round(random.uniform(1, 10), 2) for _ in range(20)]

for v in vibracoes:
    print(v)
    if v > limite:
        print("Vibração alta!")