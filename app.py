from servicios import(agregar_libro, mostrar_libro, buscar_libro, marcar_leido, eliminar_libro, estadisticas_libro)
biblioteca = []

while True:
    print("-" * 45)
    print("MENU PRINCIPAL")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Marcar como leido")
    print("5. Eliminar libro")
    print("6. Estadisticas")
    print("7. Salir")
    
    
    opcion = (input("Ingrese una opcion: \n"))
    
    print("-" * 45)
    
    if opcion == "1":
        agregar_libro(biblioteca)
    
    elif opcion == "2":
        mostrar_libro(biblioteca)
        
    elif opcion == "3":
        buscar_libro(biblioteca)
        
    elif opcion == "4":
        marcar_leido(biblioteca)
        
    elif opcion == "5":
        eliminar_libro(biblioteca)
        
    elif opcion == "6":
        estadisticas_libro(biblioteca)
        
    elif opcion == "7":
        print("Saliste, vuelve pronto!")
        break
    else:
        print("Opcion invalida, intentelo de nuevo.")
    
  