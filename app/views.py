from flask import (render_template, jsonify, make_response, current_app, send_from_directory, abort)
from app import app
import os
from werkzeug.utils import secure_filename
import secrets
from app.tasks import create_image_set
from app import q


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/about")
def about():
    return render_template("public/about.html")


@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    return render_template("public/sign_up.html")


@app.route("/json", methods=["GET", "POST"])
def json_example():
    if request.is_json():
        data = request.get_json()
        response_boddy = {
            "message": "JSON received",
            "sender": data.get("name")
        }
        response = make_response(jsonify(response_boddy), 200)
        return response
    else:
        return make_response(jsonify({"message"; "Request body has to be JSON"}), 400)


def allowed_image(filename):
    if not "." in filename:
        return False
    extension = filename.rsplit(".", 1)[1]
    if extension.upper() in current_app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


def allowed_image_filesize(filesize):
    if int(filesize) <= current_app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False
    

@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    message = None
    if request.method == "POST":
        image = request.files["image"]
        image_dir_name = secrets.token_hex(16)
        os.mkdir(os.path.join(app.config["UPLOAD_DIRECTORY"], image_dir_name))
        image.save(os.path.join(app.config["UPLOAD_DIRECTORY"], image_dir_name, image.filename))
        image_dir = os.path.join(app.config["UPLOAD_DIRECTORY"], image_dir_name)
        q.enqueue(create_image_set, image_dir, image.filename)
        flash("Image uploaded and sent for resizing", "success")
        message = "/image/{}/{}".format(image_dir_name, image.filename.split('.')[0])
    return render_template("public/upload_image.html", message=message)


@app.route("/image/<dir>/<img>")
def view_image(dir, img):
    return render_template("view_image.html", dir=dir, img=img)


@app.route("/get-image/<image_name>")
def get_image(image_name):
    try:
        return send_from_directory(current_app.config['CLIENT_IMAGES'], filename=image_name, as_attachment=True)
    except FileNotFoundError:
        abort(404)