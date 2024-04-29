from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users_list = [{
        "name": "Michał",
        "surname": "Zietkowski",
        "email": "michalzietkowski@gmail.com"
    },
    {
        "name": "Adam",
        "surname": "Bak",
        "email": "adambak@gmail.com"
    },
    {
        "name": "Piotr",
        "surname": "Nowak",
        "email": "piotr_nowak@gmail.com"
    }

]

# @app.route("/")
# def hello_world():
#     return render_template("hello_world.html")

# @app.route("/hello/")
# def hello():
#     return "Hello"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello/", defaults={"name": None})
@app.route("/hello/<name>/")
def hello_name(name):
    if name:
        return render_template("hello_name.html", rendered_name=name)
    return render_template("hello_name.html")

@app.route("/show_users/")
def show_users():
    return render_template("show_users.html", users=users_list)


@app.route("/create_user/", methods=["GET", "POST"])
def create_user():
    if request.method == "GET":
        return render_template("create_user.html")
    elif request.method == "POST":
        users_list.append({
            "name": request.form.get("name"),
            "surname": request.form.get("surname"),
            "email": request.form.get("email")
        })
        return redirect(url_for("show_users"))


if __name__ == "__main__":
    app.run(debug=True)
