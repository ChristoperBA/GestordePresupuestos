
    
import cx_Oracle
from prettytable import PrettyTable

try:
    connection = cx_Oracle.connect(
        user='ALONSO',
        password='123456',
        dsn='localhost:1521/orcl',
        encoding='UTF-8'
    )
    #orclpdb PDB$SEED
    print("Conexión exitosa")
    print("Versión de la base de datos:", connection.version)

    # Realiza operaciones en la base de datos aquí

except cx_Oracle.DatabaseError as db_error:
    print("Error de la base de datos:", db_error)

except Exception as ex:
    print("Error inesperado:", ex)


# Crear un cursor
cursor = connection.cursor()


#-----------------------CRUD RUBROS----------------------------

def create_rubro(id_rubro, nombre):
    # Insertar un nuevo registro en la tabla Rubro
    try:
        cursor.execute("INSERT INTO Rubro (ID_Rubro, Nombre) VALUES (:id_rubro, :nombre)", (id_rubro, nombre))
        connection.commit()
        print("Rubro creado exitosamente.")
    except cx_Oracle.Error as error:
        print(f"Error al crear el registro: {error}")

def read_rubros():
    # Obtener todos los registros de la tabla Rubro
    try:
        cursor.execute("SELECT * FROM Rubro")
        rows = cursor.fetchall()
        print("ID_Rubro\tNombre")
        for row in rows:
            print(f"{row[0]}\t\t{row[1]}")
    except cx_Oracle.Error as error:
        print(f"Error al leer los registros: {error}")

def update_rubro(id_rubro, new_nombre):
    # Actualizar el nombre de un rubro
    try:
        cursor.execute("UPDATE Rubro SET Nombre = :new_nombre WHERE ID_Rubro = :id_rubro", (new_nombre, id_rubro))
        connection.commit()
        print("Registro actualizado exitosamente.")
    except cx_Oracle.Error as error:
        print(f"Error al actualizar el registro: {error}")

def delete_rubro(id_rubro):
    # Eliminar un rubro por ID
    try:
        cursor.execute("DELETE FROM Rubro WHERE ID_Rubro = :id_rubro", (id_rubro,))
        connection.commit()
        print("Registro eliminado exitosamente.")
    except cx_Oracle.Error as error:
        print(f"Error al eliminar el registro: {error}")




# Ejemplos de Funcionalidad del CRUD

# Ejemplos 1
# create_rubro(21, 'Rubro1')
# create_rubro(223, 'Rubro2')
# read_rubros()

# Ejemplo 2
# update_rubro(2, 'NuevoRubro2')
# read_rubros()


# Ejemplo 3 
# delete_rubro(2)
# read_rubros()

#-----------------------FIN RUBROS----------------------------

#-----------------------CENTRO DE COSTOS----------------------------

def create_centro_de_costo(id_centro_de_costo, nombre, id_padre):
    # Insertar un nuevo registro en la tabla CentroDeCosto
    try:
        cursor.execute("INSERT INTO CentroDeCosto (ID_CentroDeCosto, Nombre, ID_Padre) VALUES (:id_centro_de_costo, :nombre, :id_padre)",
                       (id_centro_de_costo, nombre, id_padre))
        connection.commit()
        print("Registro creado exitosamente.")
    except cx_Oracle.Error as error:
        print(f"Error al crear el registro: {error}")

def read_centros_de_costo():
    # Obtener todos los registros de la tabla CentroDeCosto
    try:
        cursor.execute("SELECT * FROM CentroDeCosto")
        rows = cursor.fetchall()
        print("ID_CentroDeCosto\tNombre\t\tID_Padre")
        for row in rows:
            print(f"{row[0]}\t\t\t{row[1]}\t\t{row[2]}")
    except cx_Oracle.Error as error:
        print(f"Error al leer los registros: {error}")

def update_centro_de_costo(id_centro_de_costo, new_nombre, new_id_padre):
    # Actualizar un registro en la tabla CentroDeCosto
    try:
        cursor.execute("UPDATE CentroDeCosto SET Nombre = :new_nombre, ID_Padre = :new_id_padre WHERE ID_CentroDeCosto = :id_centro_de_costo",
                       (new_nombre, new_id_padre, id_centro_de_costo))
        connection.commit()
        print("Registro actualizado exitosamente.")
    except cx_Oracle.Error as error:
        print(f"Error al actualizar el registro: {error}")

def delete_centro_de_costo(id_centro_de_costo):
    # Eliminar un registro en la tabla CentroDeCosto por ID
    try:
        cursor.execute("DELETE FROM CentroDeCosto WHERE ID_CentroDeCosto = :id_centro_de_costo", (id_centro_de_costo,))
        connection.commit()
        print("Registro eliminado exitosamente.")
    except cx_Oracle.Error as error:
        print(f"Error al eliminar el registro: {error}")

# Ejemplo 1
# create_centro_de_costo(1, 'Centro1', 0)
# create_centro_de_costo(2, 'Centro2', 1)
# read_centros_de_costo()

# Ejemplo 2
# update_centro_de_costo(2, 'NuevoCentro2', 3)
# read_centros_de_costo()

 #Ejemplo 3
# delete_centro_de_costo(1)
# read_centros_de_costo()
  


#----------------------- FIN CENTRO DE COSTOS  ----------------------------


#-----------------------  USUARIOS  ----------------------------


def create_usuario(id_usuario, nombre, rol, id_centro_de_costo):
    # Insertar un nuevo registro en la tabla Usuario
    try:
        cursor.execute("INSERT INTO Usuario (ID_Usuario, Nombre, Rol, ID_CentroDeCosto) VALUES (:id_usuario, :nombre, :rol, :id_centro_de_costo)",
                       (id_usuario, nombre, rol, id_centro_de_costo))
        connection.commit()
        print("Registro creado exitosamente.")
    except cx_Oracle.Error as error:
        print(f"Error al crear el registro: {error}")

def read_usuarios():
    # Obtener todos los registros de la tabla Usuario
    try:
        cursor.execute("SELECT * FROM Usuario")
        rows = cursor.fetchall()
        print("ID_Usuario\tNombre\t\tRol\t\tID_CentroDeCosto")
        for row in rows:
            print(f"{row[0]}\t\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}")
    except cx_Oracle.Error as error:
        print(f"Error al leer los registros: {error}")

def update_usuario(id_usuario, new_nombre, new_rol, new_id_centro_de_costo):
    # Actualizar un registro en la tabla Usuario
    try:
        cursor.execute("UPDATE Usuario SET Nombre = :new_nombre, Rol = :new_rol, ID_CentroDeCosto = :new_id_centro_de_costo WHERE ID_Usuario = :id_usuario",
                       (new_nombre, new_rol, new_id_centro_de_costo, id_usuario))
        connection.commit()
        print("Registro actualizado exitosamente.")
    except cx_Oracle.Error as error:
        print(f"Error al actualizar el registro: {error}")

def delete_usuario(id_usuario):
    # Eliminar un registro en la tabla Usuario por ID
    try:
        cursor.execute("DELETE FROM Usuario WHERE ID_Usuario = :id_usuario", (id_usuario,))
        connection.commit()
        print("Registro eliminado exitosamente.")
    except cx_Oracle.Error as error:
        print(f"Error al eliminar el registro: {error}")

# Ejemplos 1
# create_usuario(21, 'Usuario1', 'Rol1', 1)
# create_usuario(22, 'Usuario2', 'Rol2', 2)
# read_usuarios()

# Ejemplos 2
# update_usuario(22, 'NuevoUsuario2', 'NuevoRol2', 3)
# read_usuarios()

# Ejemplos 3
# delete_usuario(21)
# read_usuarios()
#----------------------- FIN USUARIOS ----------------------------
#-----------------------  PERMISOS    ----------------------------

def create_permiso(id_permiso, id_usuario, monto_solicitado, estado, codigo_permiso, fecha, id_presupuesto):
    # Insertar un nuevo registro en la tabla Permiso
    try:
        cursor.execute("INSERT INTO Permiso (ID_Permiso, ID_Usuario, MontoSolicitado, Estado, CodigoPermiso, Fecha, ID_Presupuesto) VALUES (:id_permiso, :id_usuario, :monto_solicitado, :estado, :codigo_permiso, TO_DATE(:fecha, 'YYYY-MM-DD'), :id_presupuesto)",
                       (id_permiso, id_usuario, monto_solicitado, estado, codigo_permiso, fecha, id_presupuesto))
        connection.commit()
        print("Registro creado exitosamente.")
    except cx_Oracle.Error as error:
        print(f"Error al crear el registro: {error}")

def read_permisos():
    # Obtener todos los registros de la tabla Permiso
    try:
        cursor.execute("SELECT * FROM Permiso")
        rows = cursor.fetchall()
        print("ID_Permiso\tID_Usuario\tMontoSolicitado\tEstado\tCodigoPermiso\tFecha\t\t\tID_Presupuesto")
        for row in rows:
            print(f"{row[0]}\t\t\t{row[1]}\t\t\t{row[2]}\t\t\t{row[3]}\t{row[4]}\t\t{row[5]}\t\t{row[6]}")
    except cx_Oracle.Error as error:
        print(f"Error al leer los registros: {error}")

def update_permiso(id_permiso, new_estado):
    # Actualizar el estado de un permiso
    try:
        cursor.execute("UPDATE Permiso SET Estado = :new_estado WHERE ID_Permiso = :id_permiso", (new_estado, id_permiso))
        connection.commit()
        print("Registro actualizado exitosamente.")
    except cx_Oracle.Error as error:
        print(f"Error al actualizar el registro: {error}")

def delete_permiso(id_permiso):
    # Eliminar un permiso por ID
    try:
        cursor.execute("DELETE FROM Permiso WHERE ID_Permiso = :id_permiso", (id_permiso,))
        connection.commit()
        print("Registro eliminado exitosamente.")
    except cx_Oracle.Error as error:
        print(f"Error al eliminar el registro: {error}")

# Ejemplo 1
# create_permiso(21, 1, 5000.00, 'Pendiente', 'ABC123', '2023-01-15', 1)
# create_permiso(22, 2, 7000.00, 'Aprobado', 'DEF456', '2023-02-20', 2)
# read_permisos()
# Ejemplo 2
# update_permiso(22, 'Rechazado')
# read_permisos()
# Ejemplo 3
# delete_permiso(22)
# read_permisos()

#-----------------------  FIN PERMISOS    ----------------------------
#-----------------------  COMPRA GASTOS   ----------------------------
def create_compra_gasto(id_compra_gasto, id_permiso, numero_comprobante, monto_real, fecha):
    # Insertar un nuevo registro en la tabla CompraGasto
    try:
        cursor.execute("INSERT INTO CompraGasto (ID_CompraGasto, ID_Permiso, Numero_Comprobante, Monto_Real, Fecha) VALUES (:id_compra_gasto, :id_permiso, :numero_comprobante, :monto_real, TO_DATE(:fecha, 'YYYY-MM-DD'))",
                       (id_compra_gasto, id_permiso, numero_comprobante, monto_real, fecha))
        connection.commit()
        print("Registro creado exitosamente.")
    except cx_Oracle.Error as error:
        print(f"Error al crear el registro: {error}")

def read_compras_gastos():
    # Obtener todos los registros de la tabla CompraGasto
    try:
        cursor.execute("SELECT * FROM CompraGasto")
        rows = cursor.fetchall()
        print("ID_CompraGasto\tID_Permiso\tNumero_Comprobante\tMonto_Real\tFecha")
        for row in rows:
            print(f"{row[0]}\t\t\t{row[1]}\t\t\t{row[2]}\t\t\t\t{row[3]}\t\t{row[4]}")
    except cx_Oracle.Error as error:
        print(f"Error al leer los registros: {error}")

def update_compra_gasto(id_compra_gasto, new_monto_real):
    # Actualizar el monto real de una compra/gasto
    try:
        cursor.execute("UPDATE CompraGasto SET Monto_Real = :new_monto_real WHERE ID_CompraGasto = :id_compra_gasto", (new_monto_real, id_compra_gasto))
        connection.commit()
        print("Registro actualizado exitosamente.")
    except cx_Oracle.Error as error:
        print(f"Error al actualizar el registro: {error}")

def delete_compra_gasto(id_compra_gasto):
    # Eliminar una compra/gasto por ID
    try:
        cursor.execute("DELETE FROM CompraGasto WHERE ID_CompraGasto = :id_compra_gasto", (id_compra_gasto,))
        connection.commit()
        print("Registro eliminado exitosamente.")
    except cx_Oracle.Error as error:
        print(f"Error al eliminar el registro: {error}")

# Ejemplo 1
# create_compra_gasto(21, 1, 'ABC123', 5000.00, '2023-01-15')
# create_compra_gasto(22, 2, 'DEF456', 7000.00, '2023-02-20')
# read_compras_gastos()
# Ejemplo 2
# update_compra_gasto(2, 8000.00)
# read_compras_gastos()
# Ejemplo 3
# delete_compra_gasto(21)
# read_compras_gastos()


#----------------------- FIN COMPRA GASTOS   ----------------------------
#----------------------- MODIFICACION  ----------------------------
def create_modificacion(id_modificacion, id_presupuesto_origen, id_presupuesto_destino, monto, fecha):
    try:
        cursor.execute("""
            INSERT INTO Modificacion (ID_Modificacion, ID_PresupuestoOrigen, ID_PresupuestoDestino, Monto, Fecha)
            VALUES (:id_modificacion, :id_presupuesto_origen, :id_presupuesto_destino, :monto, TO_DATE(:fecha, 'YYYY-MM-DD'))
        """, {'id_modificacion': id_modificacion, 'id_presupuesto_origen': id_presupuesto_origen, 'id_presupuesto_destino': id_presupuesto_destino, 'monto': monto, 'fecha': fecha})
        connection.commit()
        print("Registro creado exitosamente.")
    except cx_Oracle.Error as error:
        print(f"Error al crear el registro: {error}")

def read_modificaciones():
    try:
        cursor.execute("SELECT * FROM Modificacion")
        rows = cursor.fetchall()
        print("ID_Modificacion\tID_PresupuestoOrigen\tID_PresupuestoDestino\tMonto\tFecha")
        for row in rows:
            print(f"{row[0]}\t\t\t\t{row[1]}\t\t\t\t{row[2]}\t\t\t\t\t{row[3]}\t\t{row[4]}")
    except cx_Oracle.Error as error:
        print(f"Error al leer los registros: {error}")

def update_modificacion(id_modificacion, new_monto):
    try:
        cursor.execute("UPDATE Modificacion SET Monto = :new_monto WHERE ID_Modificacion = :id_modificacion", (new_monto, id_modificacion))
        connection.commit()
        print("Registro actualizado exitosamente.")
    except cx_Oracle.Error as error:
        print(f"Error al actualizar el registro: {error}")

def delete_modificacion(id_modificacion):
    try:
        cursor.execute("DELETE FROM Modificacion WHERE ID_Modificacion = :id_modificacion", (id_modificacion,))
        connection.commit()
        print("Registro eliminado exitosamente.")
    except cx_Oracle.Error as error:
        print(f"Error al eliminar el registro: {error}")

# Ejemplo de uso
# create_modificacion(21, 1, 2, 5000.00, '2023-01-15')
# create_modificacion(22, 3, 4, 7000.00, '2023-02-20')
# read_modificaciones()
# update_modificacion(1, 6000.00)
# read_modificaciones()
# delete_modificacion(1)
# read_modificaciones()

#----------------------- FIN MODIFICACION  ----------------------------
#-----------------------    LIQUIDACION    ----------------------------
#ERROR AL LEER Y ACTUALIZAR INFO, SI AGREGA
def create_liquidacion(id_liquidacion, id_presupuesto, monto, fecha):
    try:
        cursor.execute("""
            INSERT INTO Liquidacion (ID_Liquidacion, ID_Presupuesto, Monto, Fecha)
            VALUES (:id_liquidacion, :id_presupuesto, :monto, TO_DATE(:fecha, 'YYYY-MM-DD'))
        """, {'id_liquidacion': id_liquidacion, 'id_presupuesto': id_presupuesto, 'monto': monto, 'fecha': fecha})
        connection.commit()
        print("Registro creado exitosamente.")
    except cx_Oracle.Error as error:
        print(f"Error al crear el registro: {error}")

def read_liquidaciones():
    try:
        cursor.execute("SELECT * FROM Liquidacion")
        rows = cursor.fetchall()
        print("ID_Liquidacion\tID_Presupuesto\tMonto\tFecha")
        for row in rows:
            print(f"{row[0]}\t\t\t\t{row[1]}\t\t\t\t{row[2]}\t\t{row[3]}")
    except cx_Oracle.Error as error:
        print(f"Error al leer los registros: {error}")

def update_liquidacion(id_liquidacion, new_monto):
    try:
        cursor.execute("UPDATE Liquidacion SET Monto = :new_monto WHERE ID_Liquidacion = :id_liquidacion", (new_monto, id_liquidacion))
        connection.commit()
        print("Registro actualizado exitosamente.")
    except cx_Oracle.Error as error:
        print(f"Error al actualizar el registro: {error}")

def delete_liquidacion(id_liquidacion):
    try:
        cursor.execute("DELETE FROM Liquidacion WHERE ID_Liquidacion = :id_liquidacion", (id_liquidacion,))
        connection.commit()
        print("Registro eliminado exitosamente.")
    except cx_Oracle.Error as error:
        print(f"Error al eliminar el registro: {error}")

# Ejemplo de uso
# create_liquidacion(21, 1, 2000.00, '2023-01-15')
# create_liquidacion(22, 2, 4000.00, '2023-01-20')
# read_liquidaciones()
# update_liquidacion(1, 19000.00)
# read_liquidaciones()
# delete_liquidacion(1)
# read_liquidaciones()

#-----------------------  FIN LIQUIDACION    ----------------------------

#-----------------------  MENU   ----------------------------

# def menu():
#     while True:
#         print("\nMenú de Operaciones")
#         print("1. CompraGasto")
#         print("2. Permiso")
#         print("3. Usuario")
#         print("4. CentroDeCosto")
#         print("5. Rubro")
#         print("6. Presupuesto")
#         print("7. Modificacion")
#         print("8. Liquidacion")
#         print("0. Salir")

#         try:
#             opcion = int(input("Selecciona una opción: "))
#             if opcion == 0:
#                 break
#             elif opcion == 1:
#                 # Operaciones CRUD para CompraGasto
#                 tabla = "CompraGasto"
#                 operacion = int(input(f"Operación para {tabla}: 1. Crear, 2. Leer, 3. Actualizar, 4. Eliminar: "))
#                 if operacion == 1:
#                     id_compra_gasto = int(input("ID_CompraGasto: "))
#                     id_permiso = int(input("ID_Permiso: "))
#                     numero_comprobante = input("Número de Comprobante: ")
#                     monto_real = float(input("Monto Real: "))
#                     fecha = input("Fecha (YYYY-MM-DD): ")
#                     create_compra_gasto(id_compra_gasto, id_permiso, numero_comprobante, monto_real, fecha)
#                 # Agrega casos para las otras operaciones CRUD de CompraGasto...
#             elif opcion == 2:
#                 # Operaciones CRUD para Permiso
#                 tabla = "Permiso"
#                 operacion = int(input(f"Operación para {tabla}: 1. Crear, 2. Leer, 3. Actualizar, 4. Eliminar: "))
#                 if operacion == 1:
#                     id_permiso = int(input("ID_Permiso: "))
#                     descripcion = input("Descripción: ")
#                     fecha_inicio = input("Fecha de Inicio (YYYY-MM-DD): ")
#                     fecha_fin = input("Fecha de Fin (YYYY-MM-DD): ")
#                     create_permiso(id_permiso, descripcion, fecha_inicio, fecha_fin)
#                 # Agrega casos para las otras operaciones CRUD de Permiso...
#             # Agrega casos para las otras tablas...
#             else:
#                 print("Opción no válida. Inténtalo de nuevo.")
#         except ValueError:
#             print("Error: Ingresa un número válido.")

# if __name__ == "__main__":
#     menu()
# # Cerrar el cursor y la conexión
# cursor.close()
# connection.close()
