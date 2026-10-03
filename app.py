from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/clients")
def clients():
    return render_template("clients.html")


@app.route("/infrastructure")
def infrastructure():
    return render_template("infrastructure.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO enquiries
            (name, email, phone, company, service, message)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                request.form["name"],
                request.form["email"],
                request.form["phone"],
                request.form["company"],
                request.form["service"],
                request.form["message"]
            )
        )

        conn.commit()
        conn.close()

        return redirect("/contact")

    return render_template("contact.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin123":
            return redirect("/")

    return render_template("login.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)