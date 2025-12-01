from fastapi import FastAPI
from src.interface.api.routes import training, prediction, monitoring

app = FastAPI(title="MLOps Project API", version="0.1.0")

app.include_router(training.router, prefix="/api/v1", tags=["Training"])
app.include_router(prediction.router, prefix="/api/v1", tags=["Prediction"])
app.include_router(monitoring.router, prefix="/api/v1", tags=["Monitoring"])

@app.get("/health")
def health_check():
    return {"status": "ok"}
