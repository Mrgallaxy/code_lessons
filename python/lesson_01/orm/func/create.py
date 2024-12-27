from tortoise import Tortoise

async def main():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["db.models"]},
    )
    await Tortoise.generate_schemas(safe=True)

