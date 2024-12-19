from flask import Blueprint, render_template

main = Blueprint("main", __name__)

# Home Route
@main.route("/")
def home():
    return render_template("index.html")

# About Route
@main.route("/about")
def about():
    return render_template("about.html")

# Contact Route
@main.route("/contact")
def contact():
    return render_template("contact.html")

# Portfolio Route
@main.route("/portfolio")
def portfolio():
    projects = [
        {"name": "University Management System", "description": "Efficient student record management system.", "endpoint": "project1"},
        {"name": "Amazon Product Review Sentiment Analysis", "description": "AI-powered sentiment analysis.", "endpoint": "project2"},
        {"name": "Nutritional Information Manager", "description": "Interactive nutrition tracker.", "endpoint": "project3"}
    ]
    return render_template("portfolio.html", projects=projects)

# Project Details Route
@main.route("/portfolio/<project>")
def project_detail(project):
    if project in ["project1", "project2", "project3"]:
        return render_template(f"projects/{project}.html")
    return render_template("404.html"), 404

# 404 Error Handler
@main.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
