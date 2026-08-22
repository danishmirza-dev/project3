from project3.models.subjects_model import Subject
from project3.models.teacher_model import Teacher
from project3.config.db import db
def create_subject(data):
    teacher=Teacher.query.get(data["teacher_id"])
    if not teacher:
        return {"error":"teacher not found"},404
    existing_subject=Subject.query.filter_by(name=data["name"]).first()
    if existing_subject:
        return {"error":"subject already exists"},400
    subject=Subject(
        name=data["name"],
        teacher_id=data["teacher_id"]
    )
    db.session.add(subject)
    db.session.commit()
    return subject
def  get_allsubjects(page=None,per_page=None,sort=None,filters=None):
    query=Subject.query               #all subjects,nothing is filtered

    search_filters={                  #if user gives name,we will search inside name column
        "name":Subject.name
    }
    exact_filters={
        "teacher_id":Subject.teacher_id

    }
    for key,column in search_filters.items():      #checks if user passed "name"

        value=filters.get(key)          #here filters is dict provided by route of whatever user inputs
        if value:                        #if value is found of key "name"
            query=query.filter(column.ilike(f"%{value}%"))     # it looks for Subject.name column then query is filtered,rows with subjects of similar names without case senstitive are returned
    for key,column in exact_filters.items():
        value=filters.get(key)
        if value:
            query=query.filter(column==value)   #it looks for Subject.teacher_id column, rows with exact same teacher id are returned
    if sort:                               #we must check it before,otherwise it will crash due to None.startswith...      here if sort is none is not used coz "" empty string will be treated as True case
        if sort.startswith("-"):
            field=sort[1:]            # It extracts user sort string without - and put in variable field coz our model dont have negative columns like -name,-teacher_id
            column=getattr(Subject,field,None)   #It checks if Subject model has a column named as user input strored in field, None is there in the code coz if user send "apple" then Subject.apple dosent exist will give error and with None it skips sorting
            if column:
                query=query.order_by(column.desc())
        else:
            column=getattr(Subject,sort,None)
            if column:
                query=query.order_by(column)

    if page is not None and per_page is not None:    #here is none is used because page no can be 0 sometimes and "if page" will treat as False case
        result=query.paginate(page=page,per_page=per_page)    #query is modified with paginated result like query being modified before if sort andf filter exits

    else:
        result=query.all()      #it gives all record with filter and sort if exist, without pagination

    return result
def get_subject_by_id(sid):
    subject=Subject.query.get(sid)
    if not subject:
        return {"error":"subject not found"},404
    return subject

def update(sid,data,teacher_id):
    subject=Subject.query.get(sid)
    if not subject:
        return {"error":"subject not found"},404
    if subject.teacher_id!=int(teacher_id):
        return {"message":"unauthorized access"},403

    if "teacher_id" in data:
        teacher=Teacher.query.get(data["teacher_id"])
        if not teacher:
            return {"error":"teacher not found"},404
        subject.teacher_id = data['teacher_id']


    if "name" in data:
        existing_subject=Subject.query.filter_by(name=data["name"]).first()   #it means find the subject with name we are trying to update the subject if it already exists or not
        if existing_subject and existing_subject.id!=subject.id:     #id not same means the exisiting subject is not same to the one we are trying to update name so we cant update with same name
            return {"error":"subject already exist"},400
        subject.name=data["name"]



    db.session.commit()
    return subject
def delete(sid,teacher_id):
    subject=Subject.query.get(sid)
    if not subject:
        return {"error":"subject not found"},404
    if subject.teacher_id!=int(teacher_id):
        return {"message":'unauthorized access'},403


    db.session.delete(subject)
    db.session.commit()

