from fastapi import FastAPI, Request, HTTPException,status 

from properties.application.services import InmuebleService

app = FastAPI()

@app.get("/inmuebles")
def get_inmuebles(request: Request, estado: str = None, año_construccion: str = None, ciudad: str = None):
    service = InmuebleService()
    inmuebles = service.get_inmuebles(estado, año_construccion, ciudad)    
    if inmuebles is None:        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe data para el filtro"  
        )

    # Obtener la URL completa
    base_url = str(request.base_url)
    
    # Agregar los parámetros a la URL completa
    href = f"{base_url}?estado={estado}&año_construccion={año_construccion}&ciudad={ciudad}"
    
    response = {
        "version": "v1",
        "status": "success",
        "status_code": 200,
        "message": "OK",
        "href": href,
        "data": [inmueble.__dict__ for inmueble in inmuebles]
    }
        
    return response
    