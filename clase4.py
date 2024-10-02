"""
print("Calculado Detalle de Consumo")

#Ingreso cantidad de km
kms = int(input("Ingrese la cantidad de km recorridos"))
litros_combustible = int(input("Ingrese la cantidad de lts consumidos"))
precio_por_litro = int(input("Ingrese el precio por litro de combustible"))


#Km recorridos por litro
lt_consumidos = kms / litros_combustible

#CONSUMO CADA 100km
consumo_por_100km = lt_consumidos * 100

"""





#OPERADORES RELACIONALES
#VALORES BOOLEANOS: False True

# IGUALDAD ==

x = 30
y = 50
print( 30 == 40 )#False
print( 50 == 50)#True
print( 10 == "Juan" )#False

print( x == 30 )#True
print( y == x + 10 )#False
print("Carlos" == "Carlos" )#True

#Case Sensitive
print("Juan" == "jUaN")#False 
print(" Ramon" == "Ramon ")#False




