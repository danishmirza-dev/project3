from flask_sqlalchemy import SQLAlchemy          #this SQLALchemy is not library but class provided by flask_sqlalchemy which internally uses real SQLALchemy library
db= SQLAlchemy()     # it creates a db manager object named "db" which gives access to models,columns,relationships,queries,db sessions
                     # db contains db.Model,db.Column,db.Integer,db.String,db.String





#ORM(Object Relational Mapper) converts python code in SQL automatically  through python Library SQLAlchemy that provides ORM functionality. flask_sqlalchemy connects SQLALchemy to Flask
#In other words ORM technology maps Python objects to db tables
#SQLALchemy is a python ORM library that converts python code into SQL queries
#flask_sqlalchemy is flask extension that integrates SQLAlchemy with Flask and simplifies db operations.

#when we do class Teacher(db.Model):  we are creating a Flask SQLAlchemy object
#when we did Teacher.query.all() we were using SQLAlchemy's ORM features through flask_sqlalchemy
