from flask import Flask, render_template

app = Flask(__name__)


# ==========================
# Home
# ==========================
@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# About
# ==========================
@app.route("/about")
def about():
    return render_template("about.html")


# ==========================
# Skills
# ==========================
@app.route("/skills")
def skills():
    return render_template("skills.html")


# ==========================
# Projects
# ==========================
@app.route("/projects")
def projects():
    return render_template("projects.html")


# ==========================
# Certifications
# ==========================
@app.route("/certifications")
def certifications():
    return render_template("certifications.html")


# ==========================
# Contact
# ==========================
@app.route("/contact")
def contact():
    return render_template("contact.html")


# ==========================
# Custom 404 Page
# ==========================
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


# ==========================
# Run Application
# ==========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
