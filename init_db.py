from database import engine, Base

# Crear todas las tablas definidas en models.py
print("Creando tablas en la base de datos...")
Base.metadata.create_all(bind=engine)
print("Tablas creadas exitosamente.")
