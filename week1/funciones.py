#DRY (Don't repeat yourself)
print("=== FUNCIONES ===")

def saludar(nombre):
    print(f"Hello {nombre} !!! ")

saludar("belen")

def sumar(n1=0,n2=0):
    return n1 + n2


resultado = sumar(n1=1,n2=3)
print(resultado)

def saludar2(nombre,apellido,edad):
    print(f"hola me llamo {nombre} {apellido} y tengo {edad} ")

saludar2("Pepe","Perez",30)
saludar2(edad=50,apellido="arista",nombre="belen")

print("=== ARGS ===")

