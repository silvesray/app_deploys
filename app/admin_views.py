from . import app
from flask import render_template, request, jsonify, make_response


@app.route("/admin/profile", methods=["GET", "POST"])
def profile():
    if request.is_json():
        data = request.get_json()
        print(data)
        return "JSON received", 200
    else:
        return "Request was not JSON", 400
    return render_template("admin/admin_templates.html")

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")