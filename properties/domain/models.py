from pydantic import BaseModel

class Inmueble(BaseModel):
    direccion: str
    ciudad: str
    estado: str
    precio_venta: int
    descripcion: str