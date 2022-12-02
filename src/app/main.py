from fastapi import FastAPI
from routers import cnl_api, text_to_speech, cloud_translate

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
app.include_router(text_to_speech.router)
app.include_router(cloud_translate.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to this new API Backend"}
