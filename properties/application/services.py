from ..infrastructure.repositories import InmuebleRepository

class InmuebleService:
    def __init__(self):
        self.repository = InmuebleRepository()

    def get_inmuebles(self, estado=None, año_construccion=None, ciudad=None):
        return self.repository.get_inmuebles(estado, año_construccion, ciudad)
