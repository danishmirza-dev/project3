# from flask import Blueprint,jsonify,request,abort
# from project3.services import students_services
# from project3.utils.validation import validate_student
# student_routes=Blueprint("student_routes",__name__)
# @student_routes.route("/",methods=["POST"])
# def add():
#     data=request.get_json()
#     error=validate_student(data)
#     if error:
#         abort(400,description=error)
#     student=students_services.create(data)
#     return jsonify(student.to_dict()),201
# @student_routes.route("/",methods=["GET"])
# def showall():
#     students=students_services.get()
#     return jsonify([student.to_dict() for student in students])
# @student_routes.route("/<int:sid>",methods=["GET"])
# def showbyid(sid):
#     student=students_services.get_byid(sid)
#     if not student:
#         return jsonify({"error":"student not found"})
#     return jsonify(student.to_dict())
# @student_routes.route("/<int:sid>",methods=["PUT"])
# def update(sid):
#     student=students_services.get_byid(sid)
#
#     if not student:
#         return jsonify({"error":'student not found'})
#
#     data=request.get_json()
#     error=validate_student(data)
#     if error:
#         abort(400,description=error)
#     student=students_services.update(student,data)
#     return jsonify(student.to_dict())
#
#
#
# @student_routes.route("/<int:sid>",methods=["DELETE"])
# def delete(sid):
#     student=students_services.get_byid(sid)
#     if not student:
#         return jsonify({"error": 'student not found'})
#     students_services.delete(student)
#     return jsonify({"mesasage":"deleted"})
