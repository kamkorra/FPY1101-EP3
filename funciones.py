Nombre_libros=["titulo","autor","año","sku","usuario"]

def Nombre_libros(libros):
    titulo=input("ingrese titulo de libro seleccionado:" )
    autor=input("ingrese autor del libro:" )
    ano = input("ingrese año de publicacion:" )
    sku=input("ingrese sku del libro(6 primeras letras del titulo del libro-3 primeras letras del autor-año de publicacion):").lower()

    
    libros.append({
        'titulo':titulo,
        'autor':autor,
        'año':ano,
        'sku':sku,
         })

def Prestar_libro(libros):
    usuario=input("Ingrese nombre usuario:")
    sku=input("Ingrese sku de libro:")
    Fecha_prestamo=input("Ingrese Fecha de Prestamo:")

    libros.append({'usuario':usuario})

    if Prestar_libro !=Fecha_prestamo or usuario or sku:
        print("libro disponible,reserva realizada")
    else:
        print("libro Reservado,no se encuentra disponible.")

def listar_libros(libros):
    print("listado de todos los libros:")
    print(libros)


def imprimir_reportes(libros):
    seleccion=input("")
    if seleccion== (""):
        nombreArchivo="Reportes.txt"
    with open (nombreArchivo,"w")as archivo:
        for libros in imprimir_reportes:
            archivo.write


