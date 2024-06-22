import funciones as fn

libros=[]

while True:
    print("Bienvenido al sistema de bibloteca,\n por favor seleccione su opcion")
    print("opcion 1. Registrar libro: ")
    print("opcion 2. Prestar libro:")
    print("opcion 3. Listar todos los libros: ")
    print("opcion 4. Imprimir Reporte de prestamos: ")
    print("opcion 5. Salir del programa.")

    opcion= int (input("ingrese su Opcion:"))

    if opcion == 1:
        fn.Nombre_libros(libros)
    elif opcion==2:
        fn.Prestar_libro(libros)
    elif opcion == 3:
        fn.listar_libros(libros)
        print(libros)
    elif opcion==4:
        fn.imprimir_reportes(libros)
    elif opcion==5:
        print("Programa Finalizado...\n Desarollado por Camila Quiroz \n Rut: 18.992.809-4")
        break
    else:
        print("opcion  no valida.")