sueldo=int(input("Digite su sueldo: "))
antiguedad=int(input("Digite sus años de antiguedad: "))
if sueldo<500 and antiguedad>=10:
    sueldototal1=((sueldo*20)/100)+sueldo
    print("sueldo total a pagar es: ")
    print(sueldototal1)
else:
    if sueldo<500 and antiguedad<10:
        sueldototal2=((sueldo*5)/100)+sueldo
        print("sueldo total a pagar es: ")
        print(sueldototal2)
    else:
        if sueldo>=500:
            print("sueldo total a pagar es: ")
            print(sueldo)

input()

            """ De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que lea los datos de entrada e informe:
a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.
c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios. """ 
