from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/resume/view")
def resume_view():
    return send_from_directory("static", "resume.pdf", mimetype="application/pdf", as_attachment=False)


@app.route("/resume/download")
def resume_download():
    return send_from_directory(
        "static",
        "resume.pdf",
        mimetype="application/pdf",
        as_attachment=True,
        download_name="Aasrith_Arvapalli_Resume.pdf",
    )

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)