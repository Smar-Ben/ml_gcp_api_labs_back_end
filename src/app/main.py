from fastapi import FastAPI
from routers import cnl_api

# from routers import (
# ,
# )


app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
# app.include_router(object_detected.router)
# app.include_router(inferences.router)
# app.include_router(scenario.router)
# app.include_router(pallet_info.router)
# app.include_router(aiv.router)
# app.include_router(image.router)
app.include_router(cnl_api.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to this new API Backend"}