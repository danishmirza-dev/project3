from project3.models.teacher_model import Teacher
from project3.config.db import db
def create_teacher(data):
    existing_teacher=Teacher.query.filter_by(email=data["email"]).first()
    if existing_teacher:
        return {"error":"teacher already exists"},400
    teacher_obj=Teacher(                                # A teacher_obj object is created from class Teacher
        name=data["name"],
        email=data["email"],                            #id is automatically created and subjects are created later, subjects is a relationship property not an actual column in the teacher table

        password=data["password"]
    )
    db.session.add(teacher_obj)                         #then this object is saved in db
    db.session.commit()
    return teacher_obj
def get_all_teachers():
    return Teacher.query.all()
def get_teacher_by_id(tid):
    teacher=Teacher.query.get(tid)
    if not teacher:
        return {"error":"teacher not found"},404
    return teacher

def update_teacher(tid,data):
    teacher=Teacher.query.get(tid)
    if not teacher:
        return {"error":"teacher not found"},404

    if "email" in data:
        existing_teacher=Teacher.query.filter_by(email=data["email"]).first()
        if existing_teacher and existing_teacher.id !=teacher.id:
            return {"error":"email already exists"},400
        teacher.email=data["email"]
    if "name" in data:
        teacher.name=data["name"]
    db.session.commit()
    return teacher
def delete_teacher(tid):
    teacher=Teacher.query.get(tid)
    if not teacher:
        return {"error":"teacher not found"},404
    db.session.delete(teacher)
    db.session.commit()
