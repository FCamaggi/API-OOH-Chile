from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.data.seed_rm import repo
from app.routers import assets, campaigns, compliance, faces, ingestion, territories

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description=(
        "Plataforma API-First de Inteligencia Geoespacial, Planificación Comercial "
        "y Fiscalización Normativa (Ley N° 21.473) para el inventario OOH y DOOH "
        "en las 52 comunas de la Región Metropolitana de Santiago."
    ),
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(territories.router)
app.include_router(assets.router)
app.include_router(faces.router)
app.include_router(compliance.router)
app.include_router(campaigns.router)
app.include_router(ingestion.router)


@app.get("/health", tags=["Sistema"])
def health_check() -> dict:
    return {
        "status": "ok",
        "version": settings.version,
        "mode": "IN_MEMORY_SEED" if settings.use_in_memory_db else "POSTGIS_PRODUCTION",
        "rm_communes_loaded": len(repo.communes),
        "seed_assets_loaded": len(repo.assets),
    }
