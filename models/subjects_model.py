from project3.config.db import db
class Subject(db.Model):
    id=db.Column(db.Integer,primary_key=True)   #these red lines are db constraints so wrong data never enters db even if validation is forgotten or bypassed
    name=db.Column(db.String(100),unique=True,nullable=False)
    teacher_id=db.Column(db.Integer,db.ForeignKey("teacher.id"),nullable=True)    # the value must be in teacher.id,SQLALCHEMY automatically created db table in lowercase teacher so we didnt do Teacher.idcd
    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "teacher_id":self.teacher_id

        }