from typing import NamedTuple, Optional


class Localidad(NamedTuple):
    localidad: Optional[int] = None
    id_localidad: Optional[int] = None
  


class Vivienda(NamedTuple):
    id_vivienda: Optional[int] = None
    id_casa: Optional[int] = None
    