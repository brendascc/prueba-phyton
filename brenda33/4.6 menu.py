print("HOLA USUARIO")
print("Elige una opcion...")
print("1 ..... suma")
print("2..... resta")
print("3.... multiplicar")
print("4.... comparar tres numeros")
print("5..... dividir ")
print("6..... IVA")
print("7.... tabla de multiplicar")
print("8.... salir")
a= int(input("dame tu opcion: "))
def suma(a,b):
    resul=a+b
    print("la suma de ", a, "+", b, "el resultado es ", resul)
    return
def resta(a,b):
    resul=a-b
    print("la suma de ", a, "-", b, "el resultado es ", resul)
    return
def mul(a,b):
    resul=a*b
    print("la suma de ", a, "*", b, "el resultado es ", resul)
    return
def div(a,b):
    resul=a/b
    print("la suma de ", a, "/", b, "el resultado es ", resul)
    return

def com(a,b,c):
    
    if a>b and a>c:
                print("a es el mayor de los tres")
    elif c>b and c>a:
                print("c es el mayor de todos")
    elif b>a and b>c:
                print ("b es el mayor de todos")
    if a==b and c==a:
                print ("todos son iguales")
    elif a!=b and b!=c:
                print ("todos son diferentes")
    if b==a and b!=c:
                print("b es igual a a pero diferente de c")
    elif a==c and c!=b:
                print("a es igual a c pero diferente de b")
    elif b==c and c!=a:
                print ("b es igual a c pero diferente de a")
    print ("fin")
    return
def tabla(h,k):
    for var in range (1, h+1):
        print(var, "x", k, "=", var*k)
    return
def iva(c,d,r):
    c=float(input("dame tu cantidad: "))
    d=float(input("dame el iva"))
    r=c*d
    print (r)
    return
if a==1:
    a= int(input("dame a: "))
    b=int(input("dame b: "))
    suma(a,b);
    
if a==2:
    a= int(input("dame a: "))
    b=int(input("dame b: "))
    resta(a,b);

if a==3:
    a= int(input("dame a: "))
    b=int(input("dame b: "))
    mul(a,b);
if a==4:
    a= float(input("dame a: "))
    b= float(input("dame b: "))
    c= float(input("dame c: "))
    com(a,b,c);
if a==6:
    a= int(input("dame a: "))
    b=int(input("dame b: "))
    div(a,b);

if a==5:
    c=float(input("dame tu cantidad: "))
    d=float(input("dame el iva"))
    iva(c,d,r);
    
if a==7:
    k=int(input("dame la tabla que quieres: "))
    h=int(input("hasta donde: "))
    tabla(h,k);
if a==8:
    print("fin")
    
    
    
          
    
    
