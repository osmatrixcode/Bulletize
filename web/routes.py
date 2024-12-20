from flask import render_template

def init_routes(app):
    @app.route("/", methods=["GET", "POST"])
    def index():
        return render_template("index.html")
