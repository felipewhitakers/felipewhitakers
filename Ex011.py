# Faça a medida da área e calcule a quantidade de Tinta para pintar uma parede
print("<< Meça a sua parede >>")
l1 = float(input("Digite a largura da parede: "))
l2 = float(input("Digite a altura da sua parede: "))
s = (l1 * l2)
a = (l1 * l2) / 2
print("A área da parede é: {:.3f}m²".format(s))
print("A quantidade de tinta em litros é: {:.2f}l".format(a))
