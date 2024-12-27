import asyncio
from request.request_to_db import create_user, get_user_by_username
from func.create import main

async def runs():
    await main()
    user = await create_user("user1", "pass1", "user1@example.com")

    fetched_user = await get_user_by_username("user1")
    print(f"Retrieved User: {fetched_user.username}, {fetched_user.email}")

if __name__ == "__main__":
    asyncio.run(runs())
