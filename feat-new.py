def calcular_promedio(notas):
    if not notas:
        return 0

    suma = 0

    for nota in notas:
        suma += nota

    promedio = suma / len(notas)

    if promedio >= 60:
        estado = "Aprobado"
    else:
        estado = "Reprobado"

    return promedio, estado


print(calcular_promedio([70, 80, 55, 90]))
