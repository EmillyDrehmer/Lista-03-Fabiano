producao = [100, 120, 110, 130, 90]

media = sum(producao) / len(producao)
meta = 110

print("Média:", media)

if media >= meta:
    print("Meta atingida!")
else:
    print("Meta não atingida!")