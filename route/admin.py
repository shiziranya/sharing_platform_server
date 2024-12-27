from flask import Flask,Blueprint, request, jsonify,send_from_directory,render_template
from Services.db_service import DBService
from flasgger import swag_from

admin = Blueprint("admin",__name__)

@admin.route("/get_all_post", methods=['GET'])
def get_all_post():
    """
    Get All Posts API
    ---
    description: This API retrieves all posts from the database.
    responses:
      200:
        description: Posts retrieved successfully
        schema:
          type: object
          properties:
            code:
              type: integer
              example: 200
            message:
              type: array
              items:
                type: object
                properties:
                  anger:
                    type: integer
                    example: 1
                  comment:
                    type: array
                    items:
                      type: object
                      properties:
                        angry:
                          type: integer
                          example: 4
                        content:
                          type: string
                          example: "无语"
                        id:
                          type: integer
                          example: 2
                        post_id:
                          type: integer
                          example: 1
                        uid:
                          type: integer
                          example: 5
                  content:
                    type: string
                    example: "content"
                  id:
                    type: integer
                    example: 1
                  image:
                    type: array
                    items:
                      type: string
                      example: "aaa-0.png"
                  like:
                    type: array
                    items: {}
                    example: []
                  title:
                    type: string
                    example: "aaa"
                  uid:
                    type: integer
                    example: 4
            example:
              code: 200
              message:
                - anger: 123
                  comment:
                    - angry: 4
                      content: "无语"
                      id: 2
                      post_id: 1
                      uid: 5
                    - angry: 4
                      content: "wocao"
                      id: 3
                      post_id: 1
                      uid: 5
                  content: "content"
                  id: 1
                  image:
                    - "aaa-0.png"
                    - "aaa-1.png"
                  like: []
                  title: "aaa"
                  uid: 4
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