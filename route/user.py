from flask import Flask,Blueprint, request, jsonify,send_from_directory,render_template,Blueprint
from Services.user_service import UserService

user = Blueprint("user",__name__)

@user.route('/register', methods=['POST'])
def register():
    """
    User Registration API
    ---
    description: This API allows a new user to register by providing a username, password, and profile images.
    consumes:
      - multipart/form-data
    parameters:
      - name: username
        in: formData
        type: string
        required: true
        description: The username of the user.
      - name: password
        in: formData
        type: string
        required: true
        description: The password of the user.
      - name: profile
        in: formData
        type: file
        required: true
        description: Profile images of the user. Can be multiple files.
    responses:
      200:
        description: User registered successfully
        schema:
          type: object
          properties:
            code:
              type: integer
              example: 200
            message:
              type: string
              example: "User registered successfully"
      500:
        description: Registration failed
        schema:
          type: object
          properties:
            code:
              type: integer
              example: 500
            message:
              type: string
              example: "Registration failed: Username already exists"
    """
    data = request.form
    username = data.get("username")
    password = data.get("password")
    imgs = request.files.getlist("profile")
    result,text = UserService().onUserRegister(username,password,imgs)
    if result:
        response = {
            "code":200,
            "message":text
        }
    else:
        response = {
            "code": 500,
            "message": text
        }
    return jsonify(response)



@user.route('/login', methods=['POST'])
def login():
    """
    User Login API
    ---
    description: This API allows a user to log in by providing a username and password.
    consumes:
      - application/x-www-form-urlencoded
    parameters:
      - name: username
        in: formData
        type: string
        required: true
        description: The username of the user.
      - name: password
        in: formData
        type: string
        required: true
        description: The password of the user.
    responses:
      200:
        description: User logged in successfully
        schema:
          type: object
          properties:
            code:
              type: integer
              example: 200
            message:
              type: string
              example: "User logged in successfully"
      500:
        description: Login failed
        schema:
          type: object
          properties:
            code:
              type: integer
              example: 500
            message:
              type: string
              example: "Login failed: Invalid credentials"
    """
    data = request.form
    username = data.get("username")
    password = data.get("password")
    result, text = UserService().onUserLogin(username, password)
    if result:
        response = {
            "code":200,
            "message":text
        }
    else:
        response = {
            "code": 500,
            "message": text
        }
    return jsonify(response)

@user.route('/upload', methods=['POST'])
def upload_post():
    """
    User Post Upload API
    ---
    description: This API allows a user to upload a post by providing a title, content, anger level, user ID, and images.
    consumes:
      - multipart/form-data
    parameters:
      - name: title
        in: formData
        type: string
        required: true
        description: The title of the post.
      - name: content
        in: formData
        type: string
        required: true
        description: The content of the post.
      - name: anger
        in: formData
        type: integer
        required: true
        description: The anger level of the post (as an integer).
      - name: uid
        in: formData
        type: string
        required: true
        description: The user ID of the user uploading the post.
      - name: file_imgs
        in: formData
        type: file
        required: true
        description: The images to be uploaded with the post. Can be multiple files.
    responses:
      200:
        description: Post uploaded successfully
        schema:
          type: object
          properties:
            code:
              type: integer
              example: 200
            message:
              type: string
              example: "分享上传成功"
    """
    data = request.form
    title = data.get("title")
    content = data.get("content")
    anger = int(data.get("anger"))
    uid = data.get("uid")
    imgs = request.files.getlist("file_imgs")

    img_paths = UserService().onUserUpload(title,content,anger,imgs,uid)
    response = {
        "code":200,
        "message":"分享上传成功"
    }
    return jsonify(response)

@user.route("/comment",methods=['POST'])
def upload_comment():
    """
        User Comment Upload API
        ---
        description: This API allows a user to upload a comment by providing a user ID, anger level, content, and post ID.
        consumes:
          - application/x-www-form-urlencoded
        parameters:
          - name: uid
            in: formData
            type: string
            required: true
            description: The user ID of the user uploading the comment.
          - name: angry
            in: formData
            type: string
            required: true
            description: The anger level of the comment (as a string).
          - name: content
            in: formData
            type: string
            required: true
            description: The content of the comment.
          - name: post_id
            in: formData
            type: string
            required: true
            description: The ID of the post to which the comment is being added.
        responses:
          200:
            description: Comment uploaded successfully
            schema:
              type: object
              properties:
                code:
                  type: integer
                  example: 200
                message:
                  type: string
                  example: "Comment uploaded successfully"
          500:
            description: Comment upload failed
            schema:
              type: object
              properties:
                code:
                  type: integer
                  example: 500
                message:
                  type: string
                  example: "Comment upload failed: Invalid post ID"
        """
    data = request.form
    uid = data.get("uid")
    angry = data.get("angry")
    content = data.get("content")
    post_id = data.get("post_id")
    result, text = UserService().onUserComment(uid,angry,content,post_id)
    if result:
        response = {
            "code":200,
            "message":text
        }
    else:
        response = {
            "code": 500,
            "message": text
        }
    return jsonify(response)

@user.route("/like",methods = ["POST"])
def upload_like():
    data = request.form
    uid = data.get("uid")
    post_id = data.get("post_id")
    result,text = UserService().onUserLike(uid,post_id)