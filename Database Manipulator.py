import sqlite3

class DatabaseManip:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        # Generar el string de consulta SQL para crear la tabla
        columns_string = ', '.join(columns)
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_string})"

        # Ejecutar la consulta SQL
        self.cursor.execute(create_table_query)
        self.connection.commit()
        print(f"Tabla {table_name} creada exitosamente.")

    def insert_data(self, table_name, data):
        # Generar el string de consulta SQL para insertar los datos
        placeholders = ', '.join(['?' for _ in data])
        insert_data_query = f"INSERT INTO {table_name} VALUES ({placeholders})"

        # Ejecutar la consulta SQL
        self.cursor.execute(insert_data_query, data)
        self.connection.commit()
        print("Datos insertados exitosamente.")

    def execute_query(self, query):
        # Ejecutar una consulta SQL personalizada
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    def close_connection(self):
        # Cerrar la conexión con la base de datos
        self.connection.close()
        print("Conexión cerrada.")

# Ejemplo de uso
db = DatabaseManip("newdatabase.db")  # Nombre de la base de datos

# Crear una tabla
table_name = "Estudiantes"
columns = ["id INTEGER", "nombre TEXT", "edad INTEGER"]
db.create_table(table_name, columns)

# Insertar datos en la tabla
data = (1, "Juan", 20)
db.insert_data(table_name, data)

# Consultar datos de la tabla
query = "SELECT * FROM Estudiantes"
results = db.execute_query(query)
print("Resultados de la consulta:")
for row in results:
    print(row)

# Cerrar la conexión
db.close_connection()
