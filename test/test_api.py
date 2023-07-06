from fastapi.testclient import TestClient
from fastapi import status
from main import app

client = TestClient(app)

def test_get_inmuebles():
    # Simular una solicitud GET al endpoint /inmuebles sin parámetros
    response = client.get("/inmuebles")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["version"] == "v1"
    assert response.json()["status"] == "success"
    assert response.json()["status_code"] == 200
    assert response.json()["message"] == "OK"    
    assert isinstance(response.json()["data"], list)
    # Verificar que al menos hay un inmueble en la respuesta
    assert len(response.json()["data"]) > 0
    # Verificar que cada inmueble tiene los campos esperados
    for inmueble in response.json()["data"]:
        assert "direccion" in inmueble
        assert "ciudad" in inmueble
        assert "estado" in inmueble
        assert "precio_venta" in inmueble
        assert "descripcion" in inmueble   

    # Simular una solicitud GET al endpoint /inmuebles con parámetros
    response = client.get("/inmuebles?estado=pre_venta&año_construccion=2022&ciudad=Bogotá")
    assert response.status_code == status.HTTP_200_OK

    # Verificar la estructura de la respuesta
    assert response.json().get("version") == "v1"
    assert response.json().get("status") == "success"
    assert response.json().get("status_code") == 200
    assert response.json().get("message") == "OK"    
    assert isinstance(response.json().get("data"), list)

    # Verificar que los datos de los inmuebles sean correctos
    inmuebles = response.json().get("data")
    for inmueble in inmuebles:
        assert isinstance(inmueble, dict)
        assert inmueble.get("direccion")
        assert inmueble.get("ciudad")
        assert inmueble.get("estado")
        assert inmueble.get("precio_venta")
        assert inmueble.get("descripcion")
