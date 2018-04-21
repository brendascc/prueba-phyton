a= float(input("dame a: "))
b= float(input("dame b: "))
c= float(input("dame c: "))
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
