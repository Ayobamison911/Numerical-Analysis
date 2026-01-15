from flask import Flask, request, jsonify, render_template
import math

from src.differentiation import (
    forward_difference,
    backward_difference,
    central_difference,
)
from src.integration import trapezoidal_rule, simpsons_rule
from src.roots import bisection, newton_raphson
from src.interpolation import (
    evaluate_newton_forward_third,
    newton_forward_difference_table,
)
from src.errors import (
    absolute_error,
    relative_error,
    percentage_error
)


app = Flask(__name__, template_folder="templates")


def get_function(expr):
    # Power
    expr = expr.replace("^", "**")

    # Allow trig functions without math.
    expr = expr.replace("sin(", "math.sin(")
    expr = expr.replace("cos(", "math.cos(")
    expr = expr.replace("tan(", "math.tan(")
    expr = expr.replace("exp(", "math.exp(")
    expr = expr.replace("log(", "math.log(")
    expr = expr.replace("sqrt(", "math.sqrt(")

    allowed = {
        k: v for k, v in math.__dict__.items()
        if not k.startswith("__")
    }

    def f(x):
        return eval(
            expr,
            {"__builtins__": None, "math": math},
            {**allowed, "x": x},
        )

    return f


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/differentiate", methods=["POST"])
def differentiate():
    data = request.json
    f = get_function(data["expression"])
    x = float(data["x"])
    h = float(data["h"])

    return jsonify({
        "Forward Difference": forward_difference(f, x, h),
        "Backward Difference": backward_difference(f, x, h),
        "Central Difference": central_difference(f, x, h),
    })


@app.route("/integrate", methods=["POST"])
def integrate():
    data = request.json
    f = get_function(data["expression"])
    a = float(data["a"])
    b = float(data["b"])
    n = int(data["n"])

    result = {"Trapezoidal Rule": trapezoidal_rule(f, a, b, n)}

    try:
        result["Simpson Rule"] = simpsons_rule(f, a, b, n)
    except Exception as e:
        result["Simpson Rule"] = str(e)

    return jsonify(result)


@app.route("/bisection", methods=["POST"])
def bisection_api():
    try:
        data = request.json
        f = get_function(data["expression"])
        a = float(data["a"])
        b = float(data["b"])

        root, steps = bisection(f, a, b)

        return jsonify({
            "Root": root,
            "Iterations": steps
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/newton", methods=["POST"])
def newton_api():
    try:
        data = request.json
        f = get_function(data["expression"])
        df = get_function(data["derivative"])
        x0 = float(data["x0"])

        root, steps = newton_raphson(f, df, x0)

        return jsonify({
            "Root": root,
            "Iterations": steps
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/interpolate", methods=["POST"])
def interpolate():
    data = request.json

    x_values = data["x"]
    y_values = data["y"]
    target = float(data["target"])

    if len(x_values) != len(y_values):
        return jsonify({"error": "X and Y must have same length"}), 400

    # Compute h and check equal spacing
    h = x_values[1] - x_values[0]
    for i in range(1, len(x_values) - 1):
        if round(x_values[i+1] - x_values[i], 6) != round(h, 6):
            return jsonify({"error": "X values must be equally spaced"}), 400

    x0 = x_values[0]

    table = newton_forward_difference_table(y_values)
    result = evaluate_newton_forward_third(x0, h, table, target)

    return jsonify({
        "Interpolated Value": result,
        "Difference Table": table,
        "x0": x0,
        "h": h
    })


@app.route("/error", methods=["POST"])
def error_api():
    data = request.json

    T = float(data["true"])
    A = float(data["approx"])

    # Uncertainty is OPTIONAL
    delta = float(data.get("delta", 0)) if data.get("delta") else 0.0

    # True value bounds
    T_upper = T + delta
    T_lower = T - delta

    abs_err = absolute_error(T, A)
    rel_err = relative_error(T, A)
    perc_err = percentage_error(T, A)

    result = {
        "Absolute Error": abs_err,
        "Relative Error": rel_err,
        "Percentage Error": perc_err,
    }

    # Only include range if uncertainty exists
    if delta > 0:
        result["True Value Range"] = f"[{T_lower}, {T_upper}]"

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
