from fastapi import FastAPI
from app.server.routes.freelancer import router as FreelancerRouter

app = FastAPI()

app.include_router(FreelancerRouter, tags=["Freelancer"], prefix="/freelancer")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}