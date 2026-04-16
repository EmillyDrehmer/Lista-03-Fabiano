dados = [30, 60, 90]

for d in dados:
    if d < 50:
        print("Normal")
    elif d < 80:
        print("Alerta")
    else:
        print("Crítico")