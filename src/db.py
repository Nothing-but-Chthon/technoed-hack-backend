from motor.motor_asyncio import AsyncIOMotorClient

from conf import *

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
users_collection = db[USERS_COLLECTION]
courses_collection = db[COURSES_COLLECTION]
teachers_collection = db[TEACHERS_COLLECTION]
