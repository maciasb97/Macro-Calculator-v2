# ══════════════════════════════════════════════ APP.PY ══════════════════════════════════════════════ 
# This is the main Flask app that runs the web server and handles routing.
# It imports the calculation logic from calculator.py and uses Flask to connect the backend to the frontend

from flask import Flask, render_template, request
from calculator import calculate_tdee, calculate_macros, ACTIVITY_OPTIONS, HEIGHT_OPTIONS

# Creates the Flask app. __name__ tells Flask where to look for templates/static files.
app = Flask(__name__)

# The @app.route decorator tells Flask: "when someone visits this URL, run this function"
# methods=["GET"] means this route only responds to normal page loads (typing a URL, clicking a link)
@app.route("/", methods=["GET"])

# render_template finds templates/index.html and sends it to the browser
# We pass HEIGHT_OPTIONS and ACTIVITY_OPTIONS so the HTML can build the dropdowns
def index():
    return render_template("index.html", heights=HEIGHT_OPTIONS, activities=ACTIVITY_OPTIONS)

# methods=["POST"] means this route only responds to form submissions
@app.route("/results", methods=["POST"])
def results():
    age = int(request.form["age"])  # converts the string input to an integer
    weight = int(request.form["weight"])  # converts the string input to a number (int or float)
    gender = request.form["gender"] #selects the value of the option that was chosen in the dropdown
    height = request.form["height"] #selects the value of the option that was chosen in the dropdown
    activity = request.form["activity"] #selects the value of the option that was chosen in the dropdown
    body_fat = int(request.form.get("body_fat", 0))  # default to 0 if not provided

    tdee = calculate_tdee(age, weight, gender, height, activity, body_fat)
    macros = calculate_macros(tdee)

    #send everything to results.html so it can display the TDEE and macros to the user
    return render_template("results.html", tdee=tdee, macros=macros)

#only runs if the dev server when you execute "python app.py" directly
if __name__ == "__main__":
    app.run(debug=True)  # starts the Flask dev server, debug=True means it will auto-reload on code changes