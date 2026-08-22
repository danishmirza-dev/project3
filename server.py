# print("running")
# from flask import Flask, jsonify,request
#
# from project3.routes.teachers_routes import teachers_routes
# from project3.models.teacher_model import db
# app=Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///school.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
# db.init_app(app)
# with app.app_context():
#     db.create_all()
# app.register_blueprint(teachers_routes,url_prefix="/teachers")
# @app.errorhandler(404)
# def not_found(error):
#     return jsonify({"error":"route not found"}),404
# @app.errorhandler(405)
# def method_not_allowed(error):
#     return jsonify({"error":"method not found"}),405
# @app.errorhandler(500)
# def server_error(error):
#     return jsonify({"error":"internal server error"}),500
# @app.before_request
# def before_request():
#     print(request.path,request.method)
# @app.after_request
# def after_request(response):
#     print(response.status_code)
#     return response
# if __name__=="__main__":
#     app.run(debug=True)
import os
from flask import Flask,jsonify,request
from project3.config.db import db
from flask_jwt_extended import JWTManager       # IT ADDS AUTHENTICATI0N SUPPORT TO THE APP      flask_jwt_extended is a third party  Flask package that provide jwt authentication features like token creation,token verification,route protection
from project3.routes.teachers_routes import teachers_routes       #JWT Manager is class inside package
from project3.routes.subject_routes import subject_bp

app=Flask(__name__)
app.config["JWT_SECRET_KEY"]=os.getenv(JWT_SECRET_KEY")       #USED TO CREATE JWT TOKENS
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///school.db"   # IT TELL SQLALCHEMY DATABASE ADDRESS
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False            #DIABLE UNNECESSARY CHNAGE TRACKING
db.init_app(app)                                   #CONNECTS IT TO FLASK AND  ITS DB SETTING(CONFIGURATIONS)
jwt=JWTManager(app)                           # CONNECTS JWT AUTHENTICATION TO FLASK APP. JWT MANAGER  EXTARCT TOKEM VERIFIES IT USING JWT_SECRET_KEY

app.register_blueprint(teachers_routes,url_prefix="/teachers")

app.register_blueprint(subject_bp,url_prefix="/subjects")
with app.app_context():                                    # ACTIVATE CURRENT FLASK APP,READ DB SETTINGS,CREATE ALL DB TABLES
    db.create_all()
@app.errorhandler(404)            #IT CHECKS URL INPUT RATHER THAN USER INPUT LIKE VALIDATION DOES
def route_not_found(error):
    return jsonify({"error":"route not found"}),404
@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error":'method not allowed'}),405
@app.errorhandler(500)                                  #CHECKS FOR BUG IN CODE
def server_error(error):
    return jsonify({"error":"internal server error"}),500
@app.before_request
def before_request():
    print(request.path,request.method)
@app.after_request
def after_request(response):         #when routes finishes,Flask create a response object
    print(response.status_code)
    return response
if __name__=="__main__":
    app.run(debug=False)




















