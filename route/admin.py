from flask import Flask,Blueprint, request, jsonify,send_from_directory,render_template
from Services.db_service import DBService

admin = Blueprint("admin",__name__)

@admin.route("/get_all_post", methods=['GET'])
def get_all_post():
    """
    Get All Posts API
    ---
    description: This API retrieves all posts from the database.
    """
    posts = DBService().get_posts()
    response = {
        "code": 200,
        "message": posts
    }
    return jsonify(response)

@admin.route("/get_user_post/<id>", methods=['GET'])
def get_user_post(id):
    posts = DBService().get_user_post(id)
    response = {
        "code": 200,
        "message": posts
    }
    return jsonify(response)


@admin.route("/get_user/<id>",methods = ["GET"])
def get_user(id):
    user = DBService().get_user(id)
    if user is not None:
        return jsonify({"code":200,"message":user})
    else:
        return jsonify({"code":500,"message":"用户id不存在"})


#图片链接接口
@admin.route("/upload/image/<filename>")
def uploaded_file(filename):
    return send_from_directory(admin.config['UPLOAD_FOLDER'],filename)