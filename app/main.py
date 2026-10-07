from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello DevOps Engineer"}

@app.get("/health")
def health():
    return {"status": "heathy"}

