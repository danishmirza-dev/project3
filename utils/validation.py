# def validate_teacher(data):
#     if not data:
#         return "enetr data"
#     if "name" not in data or data["name"].strip()=="" or not isinstance(data["name"],str):
#         return "enter valid name"
#     if "subject" not in data or data["subject"].strip()=="" or not isinstance(data["subject"],str):
#         return "enter valid subject"
#     return None


def validate_teacher(data):
    if not data:
        return "enter data"
    if "name" not in data or not isinstance(data["name"],str) or data["name"].strip()=="":
        return "enter valid name"

    if "email" not in data or not isinstance(data["email"],str) or data["email"].strip()=="":
        return "enter valid email"
    if '@' not in data["email"] or "." not in data["email"]:
        return "invalid email"

    return None
def validate_update_teacher(data):
    if not data:
        return "enter data"
    if "name" in data:
        if not isinstance(data["name"],str) or data["name"].strip()=="":
            return "enter valid name"
    if "email" in data:
        if not isinstance(data["email"],str) or data['email'].strip()=="":
            return "enter valid email"
        if "@" not in data["email"] or "." not in data["email"]:
            return "enter valid email"
    return None



# def validate_student(data):
#     if not data:
#         return "enetr data"
#     if "name" not in data or not isinstance(data["name"],str) or data["name"].strip()=="":
#         return "enter valid name"
#     if "age" not in data or not isinstance(data["age"],int):
#         return "ENETR VALID AGE"
#     return None
def validate_subject(data):
    if not data:
        return "enter data"
    if "name" not in data or not isinstance(data["name"],str) or data["name"].strip()=="":
        return "enter valid name"
    if "teacher_id" not in data:
        return {"error":"teacher id is required"}
    if not isinstance(data["teacher_id"],int):
        return {"error":"enter valid id"}
    return None
def validate_update_subjects(data):
    if not data:
        return "enter data"
    if "name" in data:
        if not isinstance(data["name"],str) or data["name"].strip()=="":
            return "enter valid name"
    if "teacher_id" in data:
        if not isinstance(data["teacher_id"],int):
            return "enter valid teacher id"
    return None















