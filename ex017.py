from math import hypot
co = float(input("Informe o cateto oposto: "))
ca = float(input("Informe o cateto adjacente: "))
hp = hypot(ca, co)
print("CO = {} \nCA = {} \nHipotenusa = {:.2f}".format(co, ca, hp))
