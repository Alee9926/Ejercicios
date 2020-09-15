a=int(input("Introducir coeficiente a: "))
b=int(input("Introducir coeficiente b: "))
c=int(input("Introducir coeficiente c: "))

d=int

d=(b*b)-(4*a*c)

if d>0:
    print("Las raices son reales y distintas: ")
elif d==0:
    print("Las raices son iguales")
else:
    print("Las raices son complejas o conjugadas")