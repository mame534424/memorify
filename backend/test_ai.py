import asyncio

from services.ai_service import classify_intent



async def main():

    result = await classify_intent(
        "Remind me to study tomorrow"
    )


    print(result)



asyncio.run(main())