from fastapi import FastAPI

app = FastAPI(title="RepoSense AI")

@app.get("/")
def root():
    return {"message": "RepoSense AI is running"}