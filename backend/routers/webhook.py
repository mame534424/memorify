from fastapi import APIRouter
from pydantic import BaseModel
from services.message_service import save_message
from services.ai_service import classify_intent


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
    
    intent = await classify_intent(
        text
    )


    print(intent)


    return {
        "status":"processed",
        "ai":intent
    }