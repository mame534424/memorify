from database import SessionLocal
from models.message_log import MessageLog



def save_message(
    user_id,
    content,
    direction
):

    db = SessionLocal()


    message = MessageLog(

        user_id=user_id,

        content=content,

        direction=direction

    )


    db.add(message)

    db.commit()

    db.close()