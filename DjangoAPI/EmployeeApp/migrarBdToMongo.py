import pymongo

# Conectar a la instancia de MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Crear la base de datos si no existe
db = client["EmployeeApp"]

# Crear las colecciones 'departments' y 'employees'
departments_col = db["departments"]
employees_col = db["employees"]

# Definir los esquemas para las colecciones
departments_schema = {
    "DepartmentId": 1,
    "DepartmentName": "Sales"
}

employees_schema = {
    "EmployeeId": 1,
    "EmployeeName": "John Doe",
    "Department": "Sales",
    "DateOfJoining": "2022-02-28",
    "PhotoFileName": "john-doe.jpg"
}

# Insertar los esquemas en las colecciones
departments_col.insert_one(departments_schema)
employees_col.insert_one(employees_schema)