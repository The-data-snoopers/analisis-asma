from typing import NamedTuple, Optional


class Localidad(NamedTuple):
    localidad: Optional[int] = None
    id_localidad: Optional[int] = None
  


class Vivienda(NamedTuple):
    id_vivienda: Optional[int] = None
    id_casa: Optional[int] = None



class Hacinamiento(NamedTuple):
    num_personas_hogar: Optional[int] = None
    num_cuartos_hogar: Optional[int] = None
    ocupacion: Optional[float] = None
    cantidad_asma: Optional[int] = None
    porcentaje_iluminacion: Optional[float] = None
    id_year: Optional[int] = None
    id_asma: Optional[int] = None
    id_localidad: Optional[int] = None
    id_casa: Optional[int] = None
    