from flask import Flask, render_template, request
import traceback

app = Flask(__name__)

@app.errorhandler(Exception)
def handle_exception(e):
    print(traceback.format_exc())
    return render_template("calculator.html", result="An unexpected error occurred.")

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None

    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            operation = request.form["operation"]

            if operation == "add":
                result = a + b
            elif operation == "subtract":
                result = a - b
            elif operation == "multiply":
                result = a * b
            elif operation == "divide":
                if b == 0:
                    result = "Cannot divide by zero"
                else:
                    result = a / b
        except ValueError:
            result = "Invalid input"

    return render_template("calculator.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
