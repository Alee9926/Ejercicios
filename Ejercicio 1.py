x=int(input("Introduzca un tiempo X: "))
a=int(input("Introduzca hora de trabajo: "))
b=int(input("Introduzca minuto de trabajo: "))
s=int(input("Introduzca segundo de trabajo: "))

y=int
t=int
f=int

h=a*3600
m=b*60
t=h+m+s

f=x-t


if f>0:
    print("Se puede finalizar la tarea ")
else:
    print("no se puede finalizar la tarea")