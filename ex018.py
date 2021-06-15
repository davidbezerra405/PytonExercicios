from math import cos, sin, tan, radians
ang = float(input("Informe um ângulo: "))
rad = radians(ang)
vcos = cos(rad)
vsen = sin(rad)
vtan = tan(rad)
print("Ângulo: {} \nSeno: {:.4f} \nCosseno: {:.4f} \nTangente: {:.4f}".format(ang, vsen, vcos, vtan))
