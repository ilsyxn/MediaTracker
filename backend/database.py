import os

from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel, text
from sqlmodel.ext.asyncio.session import AsyncSession

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql+asyncpg://admin:securepassword@localhost:5432/bookdb",
)

engine = create_async_engine(DATABASE_URL, echo=True)


async def get_session():
    async with AsyncSession(engine) as session:
        yield session


async def check_db_connection():
    """Verify database connectivity. Raises on failure."""
    async with AsyncSession(engine) as session:
        await session.exec(text("SELECT 1"))
