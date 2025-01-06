from flask import Flask, render_template, redirect, request
from utils.youtube_scraper import ytTranscript
import os

def init_routes(app):
    @app.route("/", methods=["GET", "POST"])
    def index():
        return render_template("index.html")




    @app.route("/url_submission", methods=["POST"])
    def url_submission_route():
        if request.method == "POST":
            yt_url = request.form.get("yt_url")
            print(yt_url)
            ytTranscript(yt_url)
            return redirect("/success")
        

    @app.errorhandler(Exception)
    def handle_all_errors(e):
        app.logger.error(f"Error occurred: {e}")
        status_code = getattr(e, 'code', 500)

        return render_template("error.html", status_code=status_code, error=str(e))



    @app.route("/success", methods=["GET"])
    def success():
        # open .txt file to read, display to /success url
        project_root = os.path.dirname(os.path.abspath(__file__))
        text_folder = os.path.join(project_root, "../text_files")
        os.makedirs(text_folder, exist_ok = True)


        file_path = os.path.join(text_folder,"llm_response.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            file_content = file.read()
        print(file_content)
        return render_template("response.html", llm_response = file_content)