
# ==========================================
# SISTEMA DE ANALISIS DE ENTREGAS DIGITALES
# TEMA 7 - RECURSIVIDAD
# ==========================================

# Lista con 8 entregas simuladas
entregas = [
    {"codigo": "1001", "archivo": "trabajo_final.pdf", "puntaje": 18, "intentos": 2},
    {"codigo": "1002", "archivo": "proyecto_v2.docx", "puntaje": 15, "intentos": 1},
    {"codigo": "1003", "archivo": "informe_final.pdf", "puntaje": 17, "intentos": 3},
    {"codigo": "1004", "archivo": "tarea_programacion.py", "puntaje": 12, "intentos": 1},
    {"codigo": "1005", "archivo": "examen_final.pdf", "puntaje": 20, "intentos": 2},
    {"codigo": "1006", "archivo": "proyecto_v2.py", "puntaje": 16, "intentos": 2},
    {"codigo": "1007", "archivo": "ejercicio_python.py", "puntaje": 14, "intentos": 1},
    {"codigo": "1008", "archivo": "trabajo_final.docx", "puntaje": 19, "intentos": 2}
]


# ==========================================
# 1. SUMATORIA RECURSIVA
# ==========================================

def sumatoria_recursiva(lista, indice=0):

    # Caso base
    if indice >= len(lista):
        return 0

    # Caso recursivo
    return lista[indice]["puntaje"] + sumatoria_recursiva(lista, indice + 1)


# ==========================================
# 2. BUSQUEDA RECURSIVA
# ==========================================

def buscar_codigo(lista, codigo, indice=0):

    # Validar codigo vacio
    if not codigo:
        return None

    # Caso base: se termino la lista
    if indice >= len(lista):
        return None

    # Si encontramos el codigo
    if lista[indice]["codigo"] == codigo:
        return lista[indice]

    # Caso recursivo
    return buscar_codigo(lista, codigo, indice + 1)


# ==========================================
# 3. CONTEO RECURSIVO DE ARCHIVOS
# ==========================================

def contar_archivos(lista, palabra, indice=0):

    # Caso base
    if indice >= len(lista):
        return 0

    # Verificar si el archivo contiene la palabra
    if palabra.lower() in lista[indice]["archivo"].lower():
        return 1 + contar_archivos(lista, palabra, indice + 1)

    # Caso recursivo
    return contar_archivos(lista, palabra, indice + 1)


# ==========================================
# 4. FACTORIAL RECURSIVO
# ==========================================

def factorial(n):

    # Validacion
    if n < 0:
        raise ValueError("No se permiten numeros negativos")

    # Caso base
    if n == 0 or n == 1:
        return 1

    # Caso recursivo
    return n * factorial(n - 1)


# ==========================================
# 5. SUMATORIA ITERATIVA
# ==========================================

def sumatoria_iterativa(lista):

    total = 0

    for entrega in lista:
        total += entrega["puntaje"]

    return total


# ==========================================
# 6. PROGRAMA PRINCIPAL Y PRUEBAS
# ==========================================

if __name__ == "__main__":

    print("SISTEMA DE ANALISIS DE ENTREGAS")
    print("--------------------------------")

    print("\nENTREGAS REGISTRADAS:")
    for entrega in entregas:
        print(entrega)

    # Prueba 1: Sumatoria recursiva
    print("\n1. SUMATORIA RECURSIVA")
    print("Resultado:", sumatoria_recursiva(entregas))

    # Prueba 2: Busqueda de codigo existente
    print("\n2. BUSQUEDA DE CODIGO EXISTENTE")
    resultado = buscar_codigo(entregas, "1004")
    print("Resultado:", resultado)

    # Prueba 3: Busqueda de codigo inexistente
    print("\n3. BUSQUEDA DE CODIGO INEXISTENTE")
    resultado = buscar_codigo(entregas, "9999")
    print("Resultado:", resultado)

    # Prueba 4: Conteo de archivos
    print("\n4. CONTEO DE ARCHIVOS CON 'final'")
    print("Cantidad:", contar_archivos(entregas, "final"))

    # Prueba 5: Factorial
    print("\n5. FACTORIAL")
    print("Factorial de 5:", factorial(5))

    # Prueba 6: Comparacion iterativa y recursiva
    print("\n6. COMPARACION DE SUMATORIAS")
    recursivo = sumatoria_recursiva(entregas)
    iterativo = sumatoria_iterativa(entregas)

    print("Resultado recursivo:", recursivo)
    print("Resultado iterativo:", iterativo)
    print("¿Los resultados coinciden?", recursivo == iterativo)

    # Prueba adicional: lista vacia
    print("\n7. PRUEBA CON LISTA VACIA")
    print("Resultado:", sumatoria_recursiva([]))

    print("\nPROGRAMA FINALIZADO")
