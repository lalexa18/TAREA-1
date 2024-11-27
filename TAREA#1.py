import sqlite3

# Crear la base de datos y la tabla si no existen
def inicializar_db():
    conexion = sqlite3.connect("recetario.db")
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recetas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            ingredientes TEXT NOT NULL,
            pasos TEXT NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()

# Agregar una nueva receta
def agregar_receta():
    nombre = input("Nombre de la receta: ")
    ingredientes = input("Ingredientes (separados por comas): ")
    pasos = input("Pasos de preparación: ")

    conexion = sqlite3.connect("recetario.db")
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO recetas (nombre, ingredientes, pasos)
        VALUES (?, ?, ?)
    """, (nombre, ingredientes, pasos))
    conexion.commit()
    conexion.close()
    print("Receta agregada con éxito.")

# Actualizar una receta existente
def actualizar_receta():
    id_receta = input("ID de la receta a actualizar: ")
    nuevo_nombre = input("Nuevo nombre de la receta: ")
    nuevos_ingredientes = input("Nuevos ingredientes (separados por comas): ")
    nuevos_pasos = input("Nuevos pasos de preparación: ")

    conexion = sqlite3.connect("recetario.db")
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE recetas
        SET nombre = ?, ingredientes = ?, pasos = ?
        WHERE id = ?
    """, (nuevo_nombre, nuevos_ingredientes, nuevos_pasos, id_receta))
    conexion.commit()
    conexion.close()
    print("Receta actualizada con éxito.")

# Eliminar una receta existente
def eliminar_receta():
    id_receta = input("ID de la receta a eliminar: ")

    conexion = sqlite3.connect("recetario.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM recetas WHERE id = ?", (id_receta,))
    conexion.commit()
    conexion.close()
    print("Receta eliminada con éxito.")

# Ver listado de recetas
def ver_recetas():
    conexion = sqlite3.connect("recetario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre FROM recetas")
    recetas = cursor.fetchall()
    conexion.close()

    if recetas:
        print("\nListado de recetas:")
        for receta in recetas:
            print(f"ID: {receta[0]} | Nombre: {receta[1]}")
    else:
        print("No hay recetas en el recetario.")

# Buscar ingredientes y pasos de una receta
def buscar_receta():
    id_receta = input("ID de la receta a buscar: ")

    conexion = sqlite3.connect("recetario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, ingredientes, pasos FROM recetas WHERE id = ?", (id_receta,))
    receta = cursor.fetchone()
    conexion.close()

    if receta:
        print("\nReceta encontrada:")
        print(f"Nombre: {receta[0]}")
        print(f"Ingredientes: {receta[1]}")
        print(f"Pasos: {receta[2]}")
    else:
        print("No se encontró la receta.")

# Menú principal
def menu():
    inicializar_db()
    while True:
        print("\n--- Libro de Recetas ---")
        print("a) Agregar nueva receta")
        print("b) Actualizar receta existente")
        print("c) Eliminar receta existente")
        print("d) Ver listado de recetas")
        print("e) Buscar ingredientes y pasos de receta")
        print("f) Salir")
        
        opcion = input("Seleccione una opción: ").lower()

        if opcion == "a":
            agregar_receta()
        elif opcion == "b":
            actualizar_receta()
        elif opcion == "c":
            eliminar_receta()
        elif opcion == "d":
            ver_recetas()
        elif opcion == "e":
            buscar_receta()
        elif opcion == "f":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
