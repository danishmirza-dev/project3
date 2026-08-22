
#
# from project3.models.student_model import Student
# from project3.config.db import db
#
#
#
# def create(data):
#     student=Student(
#         name=data["name"],
#         age=data["age"]
#     )
#     db.session.add(student)
#     db.session.commit()
#     return student
# def get():
#     return Student.query.all()
# def get_byid(sid):
#     student=Student.query.get(sid)
#     return student
# def update(student,data):
#     student.name=data["name"]
#     student.age=data["age"]
#     db.session.commit()
#     return student
# def delete(student):
#     db.session.delete(student)
#     db.session.commit()
