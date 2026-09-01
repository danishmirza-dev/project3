# from flask import Blueprint,request,jsonify,abort
# from project3.utils.validation import validate_teacher
# from project3.models.teacher_model import db, Teacher
# teachers_routes=Blueprint("teachers_routes",__name__)
# @teachers_routes.route("/",methods=["POST"])
# def add():
#     data=request.get_json()
#     error=validate_teacher(data)
#     if error:
#         abort(400,description=error)
#     teacher=Teacher(
#         name=data["name"],
#         subject=data["subject"]
#     )
#     db.session.add(teacher)
#     db.session.commit()
#     return jsonify({
#         "id":teacher.id,
#         "name":teacher.name,
#         "subject":teacher.subject
#     }),201
# @teachers_routes.route("/",methods=["GET"])
# def showall():
#     teachers=Teacher.query.all()
#     teachers_list=[]
#     for teacher in teachers:
#         teachers_list.append({
#             "id":teacher.id,
#             "name":teacher.name,
#             "subject":teacher.subject
#         })
#     return jsonify(teachers_list),200
# @teachers_routes.route("/<int:id>",methods=["GET"])
# def show_byid(id):
#     teacher=Teacher.query.get(id)
#     if not teacher:
#         return jsonify({"error":'teacher not found'}),404
#     return jsonify({
#         "id":teacher.id,
#         "name":teacher.name,
#         "subject":teacher.subject
#
#     }),200
# @teachers_routes.route("/<int:id>",methods=["PUT"])
# def update(id):
#     teacher=Teacher.query.get(id)
#     if not teacher:
#         return jsonify({"error":"teacher not found"}),404
#     data=request.get_json()
#     error=validate_teacher(data)
#     if error:
#         abort(400,description=error)
#     teacher.name=data["name"]
#     teacher.subject=data["subject"]
#     db.session.commit()
#     return jsonify({
#         "id":teacher.id,
#         "name":teacher.name,
#         "subject":teacher.subject
#     }),200
# @teachers_routes.route("/<int:id>",methods=["DELETE"])
# def delete(id):
#     teacher=Teacher.query.get(id)
#     if not teacher:
#         return jsonify({"error":'teacher not found'}),404
#     db.session.delete(teacher)
#     db.session.commit()
#     return jsonify({"message":"teacher deleted"}),200


from flask import Blueprint,jsonify,request
from flask_jwt_extended import create_access_token,create_refresh_token,jwt_required,get_jwt_identity
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import get_jwt

from project3.models.teacher_model import Teacher
from project3.services import teachers_services
from project3.utils.validation import validate_teacher,validate_update_teacher
teachers_routes=Blueprint("teachers_routes",__name__)
@teachers_routes.route("/login",methods=["POST"])
def login():
    data=request.get_json()
    email=data.get('email')
    teacher=Teacher.query.filter_by(email=email).first()
    if not teacher:
        return jsonify({"error":"teacher not found"}),404
    if not check_password_hash(teacher.password,data["password"]):
        return jsonify({"message":"incorrect password"}),401
    access_token=create_access_token(identity=str(teacher.id),
                                     additional_claims={"role":teacher.role})
    refresh_token=create_refresh_token(identity=str(teacher.id))
    return jsonify({"message":"login successfully","access_token":access_token,"refresh_token":refresh_token}),200

@teachers_routes.route("/refresh",methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    teacher_id=get_jwt_identity()
    teacher=Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({"error":"teacher not found"}),404
    new_access_token=create_access_token(identity=str(teacher.id),
                                         additional_claims={"role":teacher.role})
    return jsonify({"new_access_token":new_access_token}),200

@teachers_routes.route("/",methods=["POST"])
def add():
    data=request.get_json()
    data["password"]=generate_password_hash(data["password"])
    error=validate_teacher(data)
    if error:
        return jsonify({"error":error}),400
    teacher=teachers_services.create_teacher(data)
    if not teacher:
        return jsonify({"error":"email already exists"}),400
    return jsonify(teacher.to_dict()),201
@teachers_routes.route("/",methods=["GET"])
@jwt_required()
def getall():
    teachers=teachers_services.get_all_teachers()
    return jsonify([teacher.to_dict() for teacher in teachers]),200
@teachers_routes.route("/<int:tid>",methods=["GET"])
@jwt_required()
def getbyid(tid):
    teacher=teachers_services.get_teacher_by_id(tid)
    if isinstance(teacher,tuple):
        return jsonify(teacher[0],teacher[1])
    return jsonify(teacher.to_dict()),200
@teachers_routes.route("/<int:tid>",methods=["PUT"])
@jwt_required()
def updatebyid(tid):
    claims=get_jwt()
    if claims.get("role")!="admin":
        return jsonify({"message":"admin access required"}),403
    data=request.get_json()
    error=validate_update_teacher(data)
    if error:
        return jsonify({"error":error})
    teacher=teachers_services.update_teacher(tid,data)
    if isinstance(teacher,tuple):
        return jsonify(teacher[0],teacher[1])
    return jsonify(teacher.to_dict()),200
@teachers_routes.route("/<int:tid>",methods=["DELETE"])
@jwt_required()
def delete(tid):
    claims=get_jwt()
    if claims.get("role")!="admin":
        return jsonify({"message":'admin access required'}),403
    teacher=teachers_services.delete_teacher(tid)
    if isinstance(teacher,tuple):
        return jsonify(teacher[0],teacher[1])
    return jsonify({"message":"sucessfully deleted"}),200




















