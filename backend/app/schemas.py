from pydantic import BaseModel, ConfigDict
from typing import Optional, Dict, Any

# Esquema base para plantillas
class PlantillaBase(BaseModel):
    titulo: str
    tipo_documento: str # carta, oficio, aviso, notificacion
    cuerpo_base: str
    campos_requeridos: Optional[Dict[str, Any]] = None

# Esquema para la creación de plantillas
class PlantillaCrear(PlantillaBase):
    pass

# Esquema para las respuestas de la API al devolver una plantilla
class PlantillaRespuesta(PlantillaBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# Esquema para la solicitud de generación con IA
class GenerarDocumentoRequest(BaseModel):
    plantilla_id: int
    datos_variables: Dict[str, Any]