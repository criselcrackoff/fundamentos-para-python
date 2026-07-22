from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/celulares")  # Ruta/Path/Endpoint
async def obtenerCelulares():
    return [
        { 
            "id": 1, 
            "marca": "APPLE",
            "modelo": "iPhone 17 pro max"
        },
        {
            "id": 2, 
            "marca": "Samsung",
            "modelo": "Samsung Galaxy S25 Ultra"
        },
        {
            "id": 2, 
            "marca": "Motorola",
            "modelo": "Motorola Edge 50"
        }
    ]
