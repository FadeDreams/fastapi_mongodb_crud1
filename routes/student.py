from bson import ObjectId
from fastapi import APIRouter
import sys

sys.path.append('..')
sys.path.append('.')

from models.student import Student
from config.config_db import connection_db
from schemas.student import student_entity, list_of_student_entity

student_router = APIRouter()


@student_router.get("/students")
async def find_all_student():
    db1 = connection_db.dbtest1
    # std_coll = db1.Student
    # print(connection_db.dbtest1.Student.find_one())

    items = connection_db.dbtest1.Student.find()
    list_student_entity = []
    for item in items:
        # convert item to dic
        item_dic = {
            'id': str(item["_id"]),
            'name': item["student_name"],
            'email': item["student_email"],
            'phone': item["student_phone"]
        }
        list_student_entity.append(item_dic)
    print(list_student_entity)
    return list_student_entity


@student_router.post("/students")
async def create_student(student: Student):
    _id = connection_db.dbtest1.Student.insert_one(student.dict())
    print(_id.inserted_id)
    return _id.inserted_id


@student_router.put('/students/{student_id}')
async def update_student(student_id: str, student: Student):
    db1 = connection_db.dbtest1
    std_coll = db1.Student
    _id = std_coll.update_one({'_id': ObjectId(student_id)}, {'$set': student.dict()})
    print(_id)
    # return _id.inserted_id


@student_router.delete('/students/{student_id}')
async def delete_student(student_id: str):
    db1 = connection_db.dbtest1
    std_coll = db1.Student
    _id = std_coll.delete_one({'_id': ObjectId(student_id)})
    print(_id.inserted_id)
    return _id.inserted_id
