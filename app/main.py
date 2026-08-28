import os
from flask import Flask, request, render_template

from app.database import find_user, initialize_database
from app.commands import ping_host
from app.files import read_file
from app.auth import authenticate




app = Flask(
    __name__,
    template_folder=os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "templates"
    )
)

initialize_database()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if authenticate(username, password):
            return "Login successful"

        return "Invalid credentials", 401

    return render_template("login.html")


@app.route("/user")
def user():
    username = request.args.get("username", "")

    # INTENTIONALLY VULNERABLE: CWE-89 SQL Injection
    result = find_user(username)

    return str(result)


@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")

    # INTENTIONALLY VULNERABLE: CWE-78 OS Command Injection
    result = ping_host(host)

    return f"<pre>{result}</pre>"


@app.route("/file")
def file():
    filename = request.args.get("name", "example.txt")

    # INTENTIONALLY VULNERABLE: CWE-22 Path Traversal
    result = read_file(filename)

    return f"<pre>{result}</pre>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)