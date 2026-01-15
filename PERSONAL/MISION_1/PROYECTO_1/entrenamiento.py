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

print(f"{texto} Resultado {resultado.group()}")  # Imprime: 12345

texto = "Mi número es 12345-985"
resultado = re.search(r"\d+", texto)
print(f"{texto} Resultado {resultado.group()}")  # Imprime: 12345. Como encontró otro caracter "-", él para su proceso
