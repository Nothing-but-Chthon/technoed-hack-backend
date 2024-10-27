import uvicorn
from fastapi import FastAPI, HTTPException
from bson import json_util
from fastapi.middleware.cors import CORSMiddleware

from db import courses_collection, teachers_collection

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def get_course_by_id(course_id: int):
    course = await courses_collection.find_one({"id": course_id})
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    teacher_id = course.get("teacher_id")
    if teacher_id:
        teacher = await teachers_collection.find_one({"id": teacher_id})
        if teacher:
            course["teacher_info"] = teacher
        else:
            course["teacher_info"] = None
    else:
        course["teacher_info"] = None

    return json_util.dumps(course)


@app.get("/courses/{course_id}")
async def get_course_data(course_id: int):
    return await get_course_by_id(course_id)


@app.get("/events/{course_id}")
async def get_event_data(course_id: int):
    return await get_course_by_id(course_id)


@app.get("/courses")
async def get_courses():
    courses = courses_collection.find({"entity": "course"})
    courses = [course async for course in courses]
    return json_util.dumps(courses)


@app.get("/events")
async def get_events():
    events = courses_collection.find({"entity": "event"})
    events = [event async for event in events]
    return json_util.dumps(events)


@app.get("/teachers")
async def get_teachers():
    teachers = teachers_collection.find()
    teachers = [teacher async for teacher in teachers]
    return json_util.dumps(teachers)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host='0.0.0.0')
