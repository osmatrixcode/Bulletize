from flask import Flask, render_template, redirect, request

def init_routes(app):
    @app.route("/", methods=["GET", "POST"])
    def index():
        return render_template("index.html")

    @app.route("/url_submission", methods=["POST"])
    def url_submission_route():
        if request.method == "POST":
            yt_url = request.form.get("yt_url")
            print(yt_url)
            return redirect("/")