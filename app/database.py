from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

# Base para los modelos SQLAlchemy (se definiran en un app/models.py futuro)
Base = declarative_base()

# Creacion del motor principal a partir de la URL en configuracion
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20
)

# Fabrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db_session():
    """Generador que provee una sesion de DB por peticion."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
