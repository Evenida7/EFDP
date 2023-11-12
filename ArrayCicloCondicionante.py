mamiferos=["Tigre","León","Vaca"]
oviparos=["Tortugas", "Gallinas","Cocodrilos"]
invertebrados=["Arañas","Moluscos", "Lombrices"]
print("¿Qué especie de animal conoce?")
print()
menu="""
Menú
1. Mamíferos.
2. Ovíparos.
3. Invertebrados.
"""
print(menu)
op = int(input("Ingrese una opción: "))
if op == 1:
    for x in mamiferos:
        print(x)
elif op == 2:
    for x in oviparos:
        print(x)
elif op == 3:
    for x in invertebrados:
        print(x)
else:
    print("Opción inválida.")
