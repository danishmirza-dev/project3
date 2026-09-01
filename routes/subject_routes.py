from flask import Blueprint,request,jsonify,abort
from flask_jwt_extended import jwt_required,get_jwt_identity
from project3.services import subject_services
from project3.utils.validation import validate_subject,validate_update_subjects
subject_bp=Blueprint("subject_bp",__name__)
@subject_bp.route("/",methods=["POST"])
@jwt_required()
def add():
    data=request.get_json()
    error=validate_subject(data)
    if error:
        return jsonify({"error":error})
    subject=subject_services.create_subject(data)
    if isinstance(subject,tuple):
        return jsonify(subject[0],subject[1])
    return jsonify(subject.to_dict()),201
@subject_bp.route("/",methods=["GET"])
@jwt_required()
def showall():
    page=request.args.get("page",type=int)          #request.args contain all query paramaters in flask special obj similar like a dict {"page":"2","sort":"-name"},type=int covort str into int
    per_page=request.args.get("per_page",type=int)
    sort=request.args.get("sort")
    filters=request.args.to_dict()   #now this to_dict() convert flask object into actual dictionary so we can loop to search for filters in our service code and this to dict is flask own method
    subjects=subject_services.get_allsubjects(page=page, per_page=per_page, sort=sort, filters=filters)  #left side is parmater name and right side parameter value
    if page is not None and per_page is not None:      #this is to check if paginated data is returned by service
        return jsonify({
            "subjects":[subject.to_dict() for subject in subjects.items],
            "total":subjects.total,
            "pages":subjects.pages,
            "page":subjects.page
        })

    return jsonify([subject.to_dict() for subject in subjects]),200     #if not paginated data
@subject_bp.route("/<int:sid>",methods=["GET"])
@jwt_required()
def showbyid(sid):

    subject=subject_services.get_subject_by_id(sid)
    if isinstance(subject,tuple):
        return jsonify(subject[0],subject[1])
    return jsonify(subject.to_dict()),200
@subject_bp.route("/<int:sid>",methods=['PUT'])
@jwt_required()
def update(sid):
    teacher_id=get_jwt_identity()   #get_jwt_identity means open the token created by teacher route and give the identity i.e teacher.id
    data=request.get_json()
    error=validate_update_subjects(data)
    if error:
        abort(400,description=error)
    subject=subject_services.update(sid,data,teacher_id)
    if isinstance(subject,tuple):
        return jsonify(subject[0],subject[1])
    return jsonify(subject.to_dict()),200
@subject_bp.route("/<int:sid>",methods=["DELETE"])
@jwt_required()
def delete(sid):
    teacher_id=get_jwt_identity()
    subject=subject_services.delete(sid,teacher_id)
    if isinstance(subject,tuple):
        return jsonify(subject[0],subject[1])
    
    return jsonify({"message":'subject deleted successfully'}),200