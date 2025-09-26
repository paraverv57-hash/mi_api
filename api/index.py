from fastapi import FastAPI

app = FastAPI(title="API de prueba en Termux")

# Cache local (diccionario)
cache = {}

@app.get("/cache/{key}")
def get_cache(key: str):
    return {"key": key, "value": cache.get(key)}

@app.post("/cache/{key}/{value}")
def set_cache(key: str, value: str):
    cache[key] = value
    return {"key": key, "value": value}
