

# Numerical Analysis Software – Requirements Document

## 1. System Requirements

To successfully run the Numerical Analysis Web Application, the following system requirements must be met:

### Operating System

* Windows 8 / 10 / 11
* macOS
* Linux

###  Memory

* Minimum: 2GB RAM
* Recommended: 4GB RAM+

---

##  2. Software Requirements

###  Python

* **Python 3.10 or higher** must be installed.

Check installation by running:

```
python --version
```

If Python is not installed, download it from:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

Ensure “Add Python to PATH” is checked during installation.

---

##  3. Python Libraries Required

This application requires the following Python packages:

| Package                 | Purpose                                  |
| ----------------------- | ---------------------------------------- |
| Flask                   | Runs the web server                      |
| Math (Built-in)         | Mathematical functions                   |
| JSON Support (Built-in) | Data transfer between frontend & backend |

###  Install Dependencies

In the project root folder, run:

```
pip install flask
```

or if using pip3:

```
pip3 install flask
```

---

##  4. Project Folder Structure

Your project must follow this structure:

```
numerical_package
│
├── app.py
├── main.py   (optional CLI app)
├── templates
│     └── index.html
└── src
      ├── differentiation.py
      ├── integration.py
      ├── interpolation.py
      ├── roots.py
      └── errors.py
```

###  IMPORTANT

Inside `/src` folder there **MUST be**:

```
__init__.py
```

Even if it is empty.

It allows Python to treat `src` as a module.

---

##  5. Browser Requirements

This application runs in a web browser.

Supported Browsers:

* Google Chrome (Recommended)
* Microsoft Edge
* Firefox
* Safari

Internet is **NOT required to run the app** except for MathJax formula rendering.

If the school lab has no internet:
✔️ MathJax can be removed
✔️ App still works perfectly

---

##  6. How to Run the Application

1️. Open project folder in terminal or PowerShell
Example:

```
cd numerical_package
```

2️. Run Flask App

```
python app.py
```

3️. You will see something like:

```
 * Running on http://127.0.0.1:5000
```

4️. Open a browser and visit:

```
http://127.0.0.1:5000
```

 Application loads and is ready to use.

---

##  7. Features Supported

Application supports:

* Numerical Differentiation (FD, BD, CD)
* Root Finding (Bisection, Newton-Raphson)
* Numerical Integration (Trapezoidal, Simpson)
* Newton Forward Interpolation
* Error Analysis

  * Absolute Error
  * Relative Error
  * Percentage Error

---

##  8. Usage Constraints / Rules

* Mathematical expressions must use `x`
* Raise to power must use:

  ```
  x^2   OR   x**2
  ```
* Inputs must be **valid numbers**
* Bisection requires:

  ```
  f(a) * f(b) < 0
  ```
* Simpson Rule requires:

  ```
  n must be even
  ```

---

##  9. Common Issues & Fix

###  Flask Not Installed

```
ModuleNotFoundError: No module named flask
```

Fix:

```
pip install flask
```

###  src.errors not found

Ensure:

```
src/errors.py exists
src/__init__.py exists
```

---

##  10. Conclusion

Once the above requirements are satisfied, the Numerical Analysis Software will run smoothly and provide a fully interactive academic tool suitable for coursework, demonstrations, and practical numerical computation.

