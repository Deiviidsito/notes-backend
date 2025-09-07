from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # TODO: Cambiar a la URL de tu frontend en producciónm, para mejorar la seguridad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint basico de hello-world
@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}