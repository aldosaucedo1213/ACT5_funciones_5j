print("ejemplo de funciones")
#declarando funciones
def hola() :
    print("alguien  uso la funcion hola")

def chat(mensa):
    print(f"chat{mensa}")

def ellacontesta(mensa):
    print(f"chat ella:{mensa}")
def escribenombre(ap,n):
    print(f"tu nombre completo es :{n} {ap}")
def suma(a,b):
    s=a+b
    return s 
def resta(c,d):
    r=c-d
    return r
def multiplicacion(e,f):
    m=e*f
    return m
def division(g,h):
    d=g/h
    return d


##llamadas a funciones 
hola()
chat("que bonita estas")
ellacontesta("gracias")
escribenombre("saucedo","aldo")
print("operaciones sumas")
c1=int(input("ingresa un numero"))
c2=int(input("ingresa un numero"))
damesuma=suma(c1,c2)
print(f"la suma de {c1} + {c2} = {damesuma}")

print("operaciones resta")
c3=int(input("ingresa un numero"))
c4=int(input("ingresa un numero"))
dameresta=resta(c3,c4)
print(f"la resta de {c3} - {c4} = {dameresta}")

print("operaciones multiplicacion")
c5=int(input("ingresa un numero"))
c6=int(input("ingresa un numero"))
damemultiplicacion=multiplicacion(c5,c6)
print(f"la multiplicacion de {c5} * {c6} = {damemultiplicacion}")

print("operaciones divisiones")
c7=int(input("ingresa un numero"))
c8=int(input("ingresa un numero"))
damedivision=division(c7,c8)
print(f"la division de {c7} / {c8} = {damedivision}")
