from typing import Any, List, Optional
from beanie import init_beanie, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings, BaseModel
from models.todo import Todo


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(), document_models=[Todo])

    class Config:
        env_file = ".env"


class Database:
    def __init__(self, model) -> None:
        self.model = model

    async def save(self, document) -> None:
        await document.create()
        return

    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)

        if doc:
            return doc
        return False

    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()

        if docs:
            return docs
        return False

    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc_id = id
        doc_body = body.dict()

        doc_body = {k: v for k, v in doc_body.items() if v is not None}

        update_query = {
            "$set": {
                field: value for field, value in doc_body.items()
            }
        }

        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc

    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)

        if not doc:
            return False
        await doc.delete()
        return True
