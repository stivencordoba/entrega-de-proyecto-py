# ==============================
# SISTEMA DE TIENDA DE VIDEOJUEGOS
# ==============================

# Datos iniciales
videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    },
    "VG002": {
        "nombre": "Zelda: Breath of the Wild",
        "plataforma": "Nintendo Switch",
        "precio": 220000,
        "cantidad": 5
    },
    "VG003": {
        "nombre": "Forza Horizon 5",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8
    }
}

# ==============================
# FUNCIONES
# ==============================

def agregar_videojuego(videojuegos):
    codigo = input("Ingrese código del videojuego: ").upper()
    if codigo in videojuegos:
        print("❌ Error: El código ya existe.")
        return
    
    nombre = input("Ingrese nombre del videojuego: ")
    plataforma = input("Ingrese plataforma (PC, PlayStation, Xbox, Nintendo): ")
    
    try:
        precio = int(input("Ingrese precio: "))
        cantidad = int(input("Ingrese cantidad en inventario: "))
        if precio <= 0 or cantidad <= 0:
            print("❌ Error: Precio y cantidad deben ser mayores que cero.")
            return
    except ValueError:
        print("❌ Error: Precio y cantidad deben ser números enteros.")
        return
    
    videojuegos[codigo] = {
        "nombre": nombre,
        "plataforma": plataforma,
        "precio": precio,
        "cantidad": cantidad
    }
    print("✅ Videojuego agregado exitosamente.")


def mostrar_inventario(videojuegos):
    if not videojuegos:
        print("Inventario vacío.")
        return
    print("\n===== INVENTARIO =====")
    for codigo, datos in videojuegos.items():
        print(f"{codigo} - {datos['nombre']} ({datos['plataforma']}) - ${datos['precio']} - Cantidad: {datos['cantidad']}")


def buscar_videojuego(videojuegos):
    codigo = input("Ingrese código del videojuego: ").upper()
    if codigo in videojuegos:
        datos = videojuegos[codigo]
        print(f"\n{codigo} - {datos['nombre']} ({datos['plataforma']}) - ${datos['precio']} - Cantidad: {datos['cantidad']}")
    else:
        print("❌ Videojuego no encontrado.")


def actualizar_precio(videojuegos):
    codigo = input("Ingrese código del videojuego: ").upper()
    if codigo in videojuegos:
        try:
            nuevo_precio = int(input("Ingrese nuevo precio: "))
            if nuevo_precio > 0:
                videojuegos[codigo]["precio"] = nuevo_precio
                print("✅ Precio actualizado.")
            else:
                print("❌ El precio debe ser mayor que cero.")
        except ValueError:
            print("❌ Error: Ingrese un número válido.")
    else:
        print("❌ Videojuego no encontrado.")


def registrar_venta(videojuegos):
    codigo = input("Ingrese código del videojuego: ").upper()
    if codigo not in videojuegos:
        print("❌ Videojuego no encontrado.")
        return
    
    try:
        cantidad = int(input("Ingrese cantidad a vender: "))
        if cantidad <= 0:
            print("❌ Cantidad inválida.")
            return
    except ValueError:
        print("❌ Error: Ingrese un número válido.")
        return
    
    if cantidad > videojuegos[codigo]["cantidad"]:
        print("❌ No hay suficiente inventario.")
        return
    
    videojuegos[codigo]["cantidad"] -= cantidad
    total = cantidad * videojuegos[codigo]["precio"]
    
    print("\n===== FACTURA =====")
    print(f"Juego: {videojuegos[codigo]['nombre']}")
    print(f"Precio unitario: ${videojuegos[codigo]['precio']}")
    print(f"Cantidad: {cantidad}")
    print(f"Total: ${total}")


def mostrar_estadisticas(videojuegos):
    if not videojuegos:
        print("No hay videojuegos registrados.")
        return
    
    total_registrados = len(videojuegos)
    valor_total = sum(v["precio"] * v["cantidad"] for v in videojuegos.values())
    mas_costoso = max(videojuegos.values(), key=lambda v: v["precio"])
    mayor_stock = max(videojuegos.values(), key=lambda v: v["cantidad"])
    promedio_precio = sum(v["precio"] for v in videojuegos.values()) / total_registrados
    
    print("\n===== ESTADÍSTICAS =====")
    print(f"Total de videojuegos registrados: {total_registrados}")
    print(f"Valor total del inventario: ${valor_total}")
    print(f"Videojuego más costoso: {mas_costoso['nombre']} (${mas_costoso['precio']})")
    print(f"Videojuego con mayor cantidad: {mayor_stock['nombre']} (Cantidad: {mayor_stock['cantidad']})")
    print(f"Promedio de precios: ${promedio_precio:.2f}")


def eliminar_videojuego(videojuegos):
    codigo = input("Ingrese código del videojuego a eliminar: ").upper()
    if codigo in videojuegos:
        del videojuegos[codigo]
        print("✅ Videojuego eliminado.")
    else:
        print("❌ Videojuego no encontrado.")


def menu():
    while True:
        print("\n===== TIENDA DE VIDEOJUEGOS =====")
        print("1. Agregar videojuego")
        print("2. Mostrar inventario")
        print("3. Buscar videojuego por código")
        print("4. Actualizar precio")
        print("5. Registrar venta")
        print("6. Mostrar estadísticas")
        print("7. Eliminar videojuego")
        print("8. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_videojuego(videojuegos)
        elif opcion == "2":
            mostrar_inventario(videojuegos)
        elif opcion == "3":
            buscar_videojuego(videojuegos)
        elif opcion == "4":
            actualizar_precio(videojuegos)
        elif opcion == "5":
            registrar_venta(videojuegos)
        elif opcion == "6":
            mostrar_estadisticas(videojuegos)
        elif opcion == "7":
            eliminar_videojuego(videojuegos)
        elif opcion == "8":
            print("👋 Programa finalizado.")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

# ==============================
# EJECUCIÓN
# ==============================
menu()
