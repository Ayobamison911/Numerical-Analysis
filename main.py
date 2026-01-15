import math
import sys

from src.differentiation import (
    forward_difference,
    backward_difference,
    central_difference,
)
from src.roots import bisection, newton_raphson
from src.integration import trapezoidal_rule, simpsons_rule
from src.interpolation import (
    newton_forward_difference_table,
    evaluate_newton_forward,
)


print(sys.version)


def get_function(expr):
    # Allow ^ as power
    expr = expr.replace("^", "**")

    allowed = {
        k: v for k, v in math.__dict__.items()
        if not k.startswith("__")
    }

    def f(x):
        return eval(
            expr,
            {"__builtins__": None},
            {**allowed, "x": x}
        )

    return f


def get_derivative_function(expression):
    """
    Returns a derivative function for Newton-Raphson.
    Uses exact derivative if provided, otherwise numerical approximation.
    """
    print(
        "Note: For Newton-Raphson, providing an exact derivative is best.\n"
        "Press Enter to use numerical approximation."
    )

    df_str = input("Enter f'(x): ").strip()

    if not df_str:
        f = get_function(expression)
        return lambda x: central_difference(f, x, h=1e-5)

    return get_function(df_str)


def main():
    print("Numerical Analysis Package")
    print("==========================")

    while True:
        print("\nChoose Operation:")
        print("1. Differentiation (Forward, Backward, Central)")
        print("2. Root Finding (Bisection, Newton-Raphson)")
        print("3. Integration (Trapezoidal, Simpson's)")
        print("4. Interpolation (Newton Forward Difference)")
        print("q. Quit")

        choice = input("Option: ").strip().lower()

        if choice == "q":
            break

        try:
            if choice == "1":
                expr = input("Enter function f(x): ").strip()
                f = get_function(expr)

                x_val = float(input("Enter x point: "))
                h = float(input("Enter step size h: "))

                print(f"\nForward Diff: {forward_difference(f, x_val, h)}")
                print(f"Backward Diff: {backward_difference(f, x_val, h)}")
                print(f"Central Diff: {central_difference(f, x_val, h)}")

            elif choice == "2":
                expr = input("Enter function f(x): ").strip()
                f = get_function(expr)

                method = input(
                    "Method (b = Bisection, n = Newton-Raphson): "
                ).strip().lower()

                if method == "b":
                    a = float(input("Enter interval start a: "))
                    b_int = float(input("Enter interval end b: "))

                    root = bisection(f, a, b_int)
                    print(f"\nRoot (Bisection): {root}")

                elif method == "n":
                    df = get_derivative_function(expr)
                    x0 = float(input("Enter initial guess x0: "))

                    root = newton_raphson(f, df, x0)
                    print(f"\nRoot (Newton-Raphson): {root}")

                else:
                    print("Invalid method selected.")

            elif choice == "3":
                expr = input("Enter function f(x): ").strip()
                f = get_function(expr)

                a = float(input("Enter start a: "))
                b_int = float(input("Enter end b: "))
                n = int(
                    input("Enter number of subintervals n "
                          "(even for Simpson): ")
                )

                trap = trapezoidal_rule(f, a, b_int, n)

                try:
                    simp = simpsons_rule(f, a, b_int, n)
                except ValueError as exc:
                    simp = f"N/A ({exc})"

                print(f"\nTrapezoidal: {trap}")
                print(f"Simpson's: {simp}")

            elif choice == "4":
                print("Enter data points for Newton Forward Difference.")

                n_pts = int(input("How many points? "))
                x0 = float(input("Enter starting x0: "))
                h = float(input("Enter step size h (uniform): "))

                y_vals = []
                for i in range(n_pts):
                    val = float(input(f"Enter y for x={x0 + i * h}: "))
                    y_vals.append(val)

                table = newton_forward_difference_table(y_vals)

                print("\nDifference Table:")
                for row in table:
                    print([round(v, 4) for v in row])

                target = float(input("\nEnter target x to interpolate: "))
                result = evaluate_newton_forward(
                    x0,
                    h,
                    table,
                    target,
                )

                print(f"Interpolated value at {target}: {result}")

            else:
                print("Invalid option selected.")

        except Exception as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
