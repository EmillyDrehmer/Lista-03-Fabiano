import random

niveis = [random.randint(0, 100) for _ in range(20)]

for n in niveis:
    print(n, "%")
    if n < 20 or n > 90:
        print("Nível crítico!")