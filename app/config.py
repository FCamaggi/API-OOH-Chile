import os
from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "API-OOH-Chile — Plataforma Geoespacial y Auditoría OOH/DOOH (RM)"
    version: str = "1.0.0"
    api_prefix: str = "/v1"
    use_in_memory_db: bool = os.getenv("USE_IN_MEMORY_DB", "true").lower() == "true"
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://ooh_user:ooh_pass@localhost:5432/ooh_rm_db",
    )
    utm_value_clp: int = int(os.getenv("UTM_VALUE_CLP", "66800"))


settings = Settings()
