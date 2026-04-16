import random

vel = [round(random.uniform(0.2, 1.0), 2) for _ in range(20)]

for v in vel:
    print(v, "m/s")
    if v < 0.5:
        print("Alerta de velocidade!")