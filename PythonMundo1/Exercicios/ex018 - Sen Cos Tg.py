from math import sin,cos,tan, radians

ang = float(input('Digite um angulo: '))
seno = sin(radians(ang))
coseno = cos(radians(ang))
tangente = tan(radians(ang))
print('Seno {:.4f}, Coseno {:.4f}, Tangente {:.4f}' .format(seno, coseno, tangente))

