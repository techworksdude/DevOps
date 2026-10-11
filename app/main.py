from fastapi import FastAPI

deva = FastAPI()

@deva.get("/")
def root():
    return {"message": "Hello DevOps Engineer"}

@deva.get("/health")
def health():
    return {"status": "heathy"}



