import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error
from ..domain.models import Inmueble
from fastapi import HTTPException, status

class InmuebleRepository:
    def __init__(self):

         # Carga las variables de entorno desde el archivo .env
        load_dotenv() 

        # Obténer los valores de las variables de entorno
        self.host = os.getenv("HOST")
        self.port = os.getenv("PORT")
        self.user = os.getenv("USER")
        self.password = os.getenv("PASSWORD")
        self.schema = os.getenv("SCHEMA")

    def get_inmuebles(self, estado=None, año_construccion=None, ciudad=None):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.schema
            )
            
            cursor = conn.cursor()
            query = """
                SELECT p.id, p.address, p.city, p.price, p.description
                FROM property p
                INNER JOIN status_history sh ON p.id = sh.property_id
                INNER JOIN status s ON sh.status_id = s.id
                WHERE s.name IN ('pre_venta', 'en_venta', 'vendido')
            """
            
            if estado:
                query += f" AND s.name = '{estado}'"
            if año_construccion:
                query += f" AND p.year = {año_construccion}"
            if ciudad:
                query += f" AND p.city = '{ciudad}'"

            cursor.execute(query)
            results = cursor.fetchall()

            inmuebles = []
            
            for result in results:                
                direccion, ciudad, estado, precio_venta, descripcion = result
                if descripcion is None:
                    descripcion = ""  # Establecer un valor predeterminado si es None
                inmueble_data = {
                    "direccion": direccion,
                    "ciudad": ciudad,
                    "estado": estado,
                    "precio_venta": precio_venta,
                    "descripcion": descripcion
                }
                inmueble = Inmueble(**inmueble_data)
                inmuebles.append(inmueble)

            return inmuebles
        except Exception as e :
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Error en la consulta {e}"
            )

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
