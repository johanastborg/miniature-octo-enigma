from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Gaming Backend Active"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
