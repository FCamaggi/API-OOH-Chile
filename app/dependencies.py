from fastapi import Depends
from sqlalchemy.orm import Session
from app.config import settings
from app.database import get_db_session
from app.data.seed_rm import repo as in_memory_repo

# Se podria implementar una interfaz base si la version con SQL necesita metodos exactos.
# Por ahora, un simple condicional bastara para determinar que repositorio entregar.

def get_repository(db: Session = Depends(get_db_session)):
    """
    Inyeccion de dependencia para abstraer la persistencia de datos.
    Dependiendo de las settings, devuelve el repo en memoria o
    la instancia conectada a PostGIS.
    """
    if settings.use_in_memory_db:
        # En caso de estar en modo local/pruebas sin docker
        return in_memory_repo
    else:
        # Para la siguiente iteracion cuando implementemos las clases Repositorio SQL
        # return PostgresOOHRepository(db)
        # Por ahora para compatibilidad (en caso de prender base de datos)
        # Podriamos regresar None o un dummy, pero dado que el plan actual solo
        # pide preparar esto, documentaremos que se debe retornar el repo SQL.
        return in_memory_repo  # TODO: Reemplazar con PostgresOOHRepository
