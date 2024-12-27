from db.models import User 

async def create_user(username: str, password: str, email: str) -> User:
    user = User(username=username, password=password, email=email)
    await user.save()
    return user

async def get_user_by_username(username: str) -> User:
    user = await User.get(username=username)
    return user
