paredeAltura = float(input('Altura da parede: '))
paredeLargura = float(input('Largura da parede: '))
paredeArea = float(paredeAltura * paredeLargura)
litroTinta = float(paredeArea / 2)

print(f'Para pintar essa parede de {paredeArea:.3f}m², você gastará {litroTinta:.2f}L de tinta.')


