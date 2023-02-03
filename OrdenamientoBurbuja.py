def ordenar_pacientes():
    pacientes = [{'nombre': 'Juan', 'gravedad': 3},
                 {'nombre': 'Maria', 'gravedad': 1},
                 {'nombre': 'Pedro', 'gravedad': 2}]
    for i in range(len(pacientes)-1,0,-1):
        for j in range(i):
            if pacientes[j]['gravedad'] > pacientes[j+1]['gravedad']:
                pacientes[j], pacientes[j+1] = pacientes[j+1], pacientes[j]
    print(pacientes)

ordenar_pacientes()