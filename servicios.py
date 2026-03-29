
def agregar_libro (biblioteca):
    #agregar nombre del libro
    valido = False
    while not valido: #operador logico
        titulo = input("Ingrese el nombre del libro: \n")
        if titulo.replace(" ", "").isalpha():
            valido = True
        else:
            print("Solo puede ingresar letras, intente de nuevo.")
            
    #agregar nombre del autor
    valido = False
    while not valido:
        autor = input("Ingrese el nombre del autor: \n")
        
        if autor.replace(" ", "").isalpha(): #leonardo jimenez
            valido = True #se detiene solo, si se cumple la funcion
        else: #leo 23
            print("Solo puede ingresar letras, intente de nuevo. ")
    
    #total paginas del libro
    
    valido = False #empezxamos como falso osea que todavia no es valido
    while not valido: #mientras no sea valido sigue pidiendo (osea, mientras que valido no sea True, sigue intentando. )                                      
        try:
            paginas = int(input("Ingrese el numero total de paginas: \n "))
            if paginas < 0:
                print("El numero debe ser positivo, intente de nuevo. ")
            else:
                valido = True #ahora si es valido, el while se detiene solo
        except:
            print("Valor invalido, intente nuevamente. ") #decimales ej: 3.9 paginas
            
    libros = {"titulo": titulo, "autor": autor, "paginas": paginas, "leido": False}
    biblioteca.append(libros)
    print(f"El libro: {titulo} fue agregado correctamente!") #interpolacion de cadenas
            
def mostrar_libro (biblioteca):
    if len(biblioteca) == 0:
        print("No hay nada en la biblioteca, ingrese un libro.")  
    else:
        print("Biblioteca actual: ")
        print("-" * 45)
        for libros in biblioteca:
            print("-" * 45)
            print(f"  Titulo:    {libros['titulo']}")
            print(f"  Autor:     {libros['autor']}")
            print(f"  Paginas:   {libros['paginas']}")
            print(f"  Leido:     {libros['leido']}")
            print("-" * 45)

def buscar_libro (biblioteca):
    nombre = input("Ingrese el nombre del libro a buscar: \n")
    
    for libros in biblioteca:
        if libros['titulo'].lower() == nombre.lower():
            print("Libro encontrado:")
            print("-" * 45)
            print(f"  Titulo:    {libros['titulo']}")
            print(f"  Autor:     {libros['autor']}")
            print(f"  Paginas:   {libros['paginas']}")
            print(f"  Leido:     {libros['leido']}")
            print("-" * 45)
            return libros
        
    print(f"Libro: {nombre} no encontrado.") # se ejecuta solo si el for terminó sin encontrar nada, es bueno dejarlo afuera del for 
    return None
        
def marcar_leido (biblioteca):
    nombre = input("Ingrese el nombre del libro a marcar como leido: \n")
    
    for libros in biblioteca:
        if libros['titulo'].lower() == nombre.lower():
            libros['leido'] = True
            print(f"El libro {nombre} fue marcado como leido. ")
            """
            Sin el return el for seguiría recorriendo el resto de la biblioteca aunque ya encontró el libro. No causaría un error pero marcaría como leído el libro correcto y luego seguiría revisando los demás innecesariamente. El return sirve para decirle "ya encontraste lo que buscabas, para".
            """
            return
    print(f"El libro {nombre} no fue encontrado. ")        

def eliminar_libro (biblioteca):
    nombre = input("Ingresa el nombre del libro a eliminar: \n")
    
    for libros in biblioteca:
        if libros['titulo'].lower() == nombre.lower():
            biblioteca.remove(libros)
            print(f"Libro: {nombre} eliminado correctamente! ")
            return
    print(f"El libro: {nombre} no fue encontrado en la biblioteca.")
    
def estadisticas_libro (biblioteca):
    if len(biblioteca) == 0:
        print("La biblioteca esta vacia.")
    else:
        #total de libros
        total = len(biblioteca)
        
        #leidos
        leidos = sum(1 for l in biblioteca if l['leido'] == True)
        
        #no leidos
        no_leidos = sum(1 for l in biblioteca if l['leido'] == False)
        
        #Libro con mas paginas
        mas_paginas = max(biblioteca, key=lambda l: l['paginas'])
        
        #Total de paginas
        total_paginas = sum(l['paginas'] for l in biblioteca)
        
        print("\n ESTADÍSTICAS:")
        print("-" * 45)
        print(f"Total de libros:      {total}")
        print(f"Leidos:               {leidos}")
        print(f"No leidos:            {no_leidos}")
        print(f"Libro con mas paginas: {mas_paginas['titulo']} ({mas_paginas['paginas']} paginas)")
        print(f"Total de paginas:     {total_paginas}")
        print("-" * 45)