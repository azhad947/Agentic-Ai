from fastapi import FastAPI
from pydantic import BaseModel
from .agents import WaterIntakeAget
from .logger import log_message


app = FastAPI()

agent = WaterIntakeAget()

class WaterIntakeRequest(BaseModel):
    user_id: str
    intake_ml: int

@app.post('/log-intake')
async def log_wate_intake(request: WaterIntakeRequest):
    log_intake(request.user_id , request.intake_ml)
    analysis = WaterIntakeAget().analyze_intake(request.intake_ml)
    log_message(f"user {request.user_id} with intake {request.intake_ml}")
    return {"message":"water intake logged successfully " , "analysis" : analysis }


@app.get('/get-intake-history')
async def get_intake_history(userId: int):
    get_history(userId)