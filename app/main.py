from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="RepoSense AI")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "RepoSense AI is running"}