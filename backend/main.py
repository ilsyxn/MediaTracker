from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import check_db_connection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World", "TechStack": "FastAPI + Docker + uv"}

@app.get("/health")
async def health():
    try:
        await check_db_connection()
        return {"status": "healthy", "database": "reachable"}
    except Exception:
        return {"status": "unhealthy", "database": "unreachable"}