import re # Importar el módulo de expresiones regulares. Esta es una librería estándar de Python que permite trabajar con patrones en cadenas de texto.´


"""
Expresiones regulares en Python
Problemas reales
""" 

print("Librería cargada correctamente")

# Ejemplo 1

texto = "Mi número es 12345"
resultado = re.search(r"\d+", texto)  # Buscar una secuencia de dígitos en el texto
# r=read
# \d+ = expresión regular para encontrar números (dígitos) en una cadena de texto

#\d → cualquier dígito (0–9)
#+ → uno o más
#r → cadena cruda (evita problemas con \)

print(f"{texto} Resultado {resultado.group()}")  # Imprime: 12345 - Aquí asume los espcios, los toma, no los borra

texto = "Mi número es 12345-985"
resultado = re.search(r"\d+", texto)
print(f"{texto} Resultado {resultado.group()}")  # Imprime: 12345. Como encontró otro caracter "-", él para su proceso

texto = "Mi número es 12345-985"
resultado = re.findall(r"\d+", texto)
print(f"{texto} Resultado {resultado}")  # Imprime: ['12345', '985']. Aquí encuentra todos los números en la cadena de texto, es decir es una lista en un string

texto = "Mi número es 123*45-985"
resultado = re.findall(r"\d+", texto)
print(f"{texto} Resultado {resultado}") # Imprime: ['123', '45', '985']. Aquí encuentra todos los números en la cadena de texto, es decir es una lista en un string
# Esto es usado en +57 para separar los números telefónicos, él toma los números y elimina los caracteres especiales 

documento = "cc.75.077.60"

def clean_id(documentos): 
    # def para declarar una función en python (palabra reservada)
    # clean_id es el nombre de la función
    return re.sub(r"\D", "", documentos) 
    # D → cualquier carácter que no sea un dígito o número
    # sub → sustituir
    # "" → por nada, reemplazar por nada
    # r →  cadena cruda (evita problemas con \)
    # documentos → parámetro de la función
    # " " → aquí hay 1 caracter, es un espacio en blanco
    # "" → aquí no hay nada, es vacío

print(clean_id(documento))  # Imprime: 7507760 - Aquí elimina los puntos y deja solo los números



