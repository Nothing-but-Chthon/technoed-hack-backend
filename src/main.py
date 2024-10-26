from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from motor.motor_asyncio import AsyncIOMotorClient
from bson import json_util


from conf import *

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
users_collection = db[USERS_COLLECTION]
courses_collection = db[COURSES_COLLECTION]
teachers_collection = db[TEACHERS_COLLECTION]

app = FastAPI()

class UserModel(BaseModel):
    user_id: int = Field(alias="_id")
    first_name: str
    phone_number: str


async def get_user_by_id(user_id: int):
    return await users_collection.find_one({"_id": user_id})

@app.post("/add_user")
async def add_user(user_data: UserModel):
    await users_collection.update_one(
        {"_id": user_data.user_id},
        {"$set": user_data.model_dump()},
        upsert=True
    )
    print(user_data)
    print(await get_course_data(12345))
    print()
    
    print(await get_teachers())


@app.get("/course/info")
async def get_course_data(course_id):
    course = await courses_collection.find_one({"id": course_id})
    teacher_id = course.get("teacher_id")   
    if teacher_id:
        teacher = await teachers_collection.find_one({"id": teacher_id})
        if teacher:
            course["teacher_info"] = teacher
        else:
            course["teacher_info"] = None
    else:
        course["teacher_info"] = None

    return course


@app.get("/courses")
async def get_courses():
    courses = courses_collection.find({"event": False})
    courses = [course async for course in courses]
    return json_util.dumps(courses)

@app.get("/events")
async def get_events():
    events = courses_collection.find({"event": True})
    events = [event async for event in events]
    return json_util.dumps(events)

@app.get("/teachers")
async def get_teachers():
    teachers = teachers_collection.find()
    teachers = [teacher async for teacher in teachers]
    return json_util.dumps(teachers)

