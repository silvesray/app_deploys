from flask import (render_template, jsonify, make_response, current_app, send_from_directory)
from app import app
import os
from werkzeug.utils import secure_filename


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
    if request.method == "POST":
        if request.files:
            if "filesize" in request.cookies:
                if not allowed_image_filesize(request.cookies["filesize"]):
                    print("Filesize exceed maximum limit")
                    return redirect(request.url)
                images = request.files["image"]
                
                if images.filename == "":
                    print("No filename")
                    return redirect(request.url)
                
                if allowed_image(images.filename):
                    filename = secure_filename(images.filename)
                    images.save(os.path.join(current_app.config["IMAGE_UPLOADS"], filename))
                    print("Image saved")
                    return redirect(request.url)
                else:
                    print("That file extension is not allowed")
                    return redirect(request.url)
    return render_template("public/upload_image.html")


@app.route("/get-image/<image_name>")
def get_image(image_name):
    try:
        return send_from_directory(current_app.config['CLIENT_IMAGES'], filename=image_name, as_attachment=True)
    except FileNotFoundError:
        abort(404)