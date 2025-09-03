# подключение к базе данных

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmarker

from app.core.config import settings

engine = create_async_engine(settings.db_url, echo=settings.DEBUG, future=True)

async_session_marker = sessionmarker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

# FastAPI


async def get_db() -> AsyncSession:
    async with async_session_marker() as session:
        yield session
