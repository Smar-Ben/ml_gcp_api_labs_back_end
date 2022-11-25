from functools import lru_cache

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    APP_NAME: str = "API"
    ENV_NAME: str = "dev"
    AIV_URI: str = Field(env="AIV_URI")
    DATASTORE_NAMESPACE: str = Field(env="DATASTORE_NAMESPACE", default="")
    aiv_get_vehicle_info: str = Field(
        env="AIV_GET_VEHICULE_INFO", default="getVehicleInfo"
    )
    aiv_assign_pickup: str = Field(env="AIV_ASSIGN_PICKUP", default="assignPickup")
    aiv_get_status: str = Field(env="AIV_GET_STATUS", default="getStatus")
    aiv_update_status: str = Field(env="AIV_UPDATE_STATUS", default="updateStatus")
    cert_path: str = Field(..., env="CERT_PATH")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
