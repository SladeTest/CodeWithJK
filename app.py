from flask import Flask, render_template

app = Flask(__name__)

# Course data (expanded)
courses = {
    "12month": [
        {
            "title": "Phase 1: Foundations", 
            "months": "1-4", 
            "topics": ["Python Basics", "OOP", "APIs", "Pandas"],
            "icon": "bi-code-square"  # Bootstrap Icons class
        },
        {
            "title": "Phase 2: Specialization", 
            "months": "5-8", 
            "topics": ["Machine Learning", "Deep Learning", "NLP"],
            "icon": "bi-robot"
        },
        {
            "title": "Phase 3: Projects", 
            "months": "9-12", 
            "topics": ["Capstone Project", "Deployment", "Portfolio"],
            "icon": "bi-rocket"
        }
    ],
    "4month": [
        {
            "title": "Month 1", 
            "topics": ["Python Crash Course", "OOP", "Automation"],
            "icon": "bi-speedometer2"
        },
        {
            "title": "Month 2", 
            "topics": ["Choose Path: Data Science, ML, or Automation"],
            "icon": "bi-signpost-split"
        },
        {
            "title": "Month 3", 
            "topics": ["Advanced Project", "EDA or Model Training"],
            "icon": "bi-gear"
        },
        {
            "title": "Month 4", 
            "topics": ["Deployment", "Resume Prep"],
            "icon": "bi-cloud-upload"
        }
    ]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/12month")
def full_course():
    return render_template("12month.html", course=courses["12month"])

@app.route("/4month")
def fast_track():
    return render_template("4month.html", course=courses["4month"])

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)