from pydantic import BaseModel


def student_entity(item) -> dict:
    return {
        'id': str(item["_id"]),
        'name': item["student_name"],
        'email': item["student_email"],
        'phone': item["student_phone"]
    }


def list_of_student_entity(items) -> list:
    list_student_entity = []
    for item in items:
        list_student_entity.append(student_entity(item))
    return list_student_entity
