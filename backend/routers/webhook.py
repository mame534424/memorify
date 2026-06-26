from fastapi import APIRouter
from pydantic import BaseModel
from services.message_service import save_message


router = APIRouter()



class TelegramMessage(BaseModel):

    update_id: int

    message: dict



@router.post("/webhook/telegram")
async def telegram_webhook(
    data: TelegramMessage
):

    text = data.message.get("text")
    
    #save message to database
    save_message(
        user_id=None,
        content=text,
        direction="inbound"
    )
    
    print (f"Received message: {text}")

    return {
        "status":"received"
    }