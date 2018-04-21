print("HOLA USUARIO")
print("Elige una opcion...")
print("0 si quieres comparar dos numeros")
print("1:si quieres sumar")
print("2: si quieres restar")
print("3: si quieres imprimir mis datos")
print("4: si quieres multiplicar")
print("5: si quieres sacar una tabla")
print("6: si quieres dividir")
print("7: salir")
a= int(input("dame tu opcion: "))
if a==0:
    k=int(input("dame a"))
    h=int(input("dame b:"))
    if k==h:
          print("los numeros son iguales")
    else:
          print("los numeros son diferentes")

    
if a==1:
    k=int(input("dame a"))
    h=int(input("dame b:"))
    j=k+h
    print(j)
if a==2:
    k=int(input("dame a"))
    h=int(input("dame b:"))
    j=k-h
    print(j)
if a==3:
    k=int(input("dame tu nombre: "))
    h=int(input("dame tu edad: "))
    j=int(input("dame tu pesa"))
    print(k,h,j)
if a==4:
    k=int(input("dame a"))
    h=int(input("dame b:"))
    j=k*h
    print(j)
if a==6:
    k=int(input("dame a: "))
    h=int(input("dame b: "))
    j=k/h
    print (j)
if a==5:
    k=int(input("dame la tabla que quieres: "))
    h=int(input("hasta donde: "))
    for var in range (1, h+1):
        print(var, "x", k, "=", var*k)
    
if a==7:
    print("FINALIZADO")
    
    
