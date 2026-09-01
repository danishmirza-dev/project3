# from flask_sqlalchemy import SQLAlchemy
# db=SQLAlchemy()
# class Teacher(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(100),nullable=False)
#     subject=db.Column(db.String(100),nullable=False)


from project3.config.db import db
class Teacher(db.Model):
    id=db.Column(db.Integer,primary_key=True)     #id,name etc are special class attributes describing db columns
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),unique=True,nullable=False)
    password=db.Column(db.String(100),nullable=False)
    subjects=db.relationship('Subject',backref='teacher',lazy=True,cascade="all, delete")  # one teacher can access all *his* subjects,lazy=dont load subjects unless teacher.subject
    role=db.Column(db.String(20),nullable=False,default="teacher")                                                                                     #backref creates reverse relationship also means without it
                                                                                           #teacher.subject works but subject.teacher wont work,casade=if teacher is deleted, delete all his subjects too
    def to_dict(self):
        return {                                     # Route calls to_dict method like object.to_dict() and that object is passed to self
            "id":self.id,                                 # to convert python object into dictionary to fetch later
            "name":self.name,
            "email":self.email,
            "subjects":[subject.name for subject in self.subjects]
            
        }



















