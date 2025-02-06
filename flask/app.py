from flask import Flask, render_template, request

app = Flask(__name__)


# Attach a decorator to the function that handles the route
@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/intro", methods=["GET", "POST"])
@app.route("/intro/<username>")
def intro(username=None):
    print(request.args)
    username = request.args.get("username", "User")
    password = request.args.get("password", "1234")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        fullname = request.form.get("fullname")

        print(username, password, fullname)

    # Check if credentials are correct

    if username:
        return f"Hello, {username}"
    else:
        return "Hello, User"


@app.route("/about/<username>/<address>/<color>")
def about(username, address, color):
    return f"Hi, my name is {username} and I live in {address}. My favourite colour is {color}"


@app.route("/listings.html")
def listings():
    return render_template(
        "default_page.html",
        page_title="View All Products",
        page_header="All Products",
        page_text="We have a wide selection of products to meet the requirements of all.",
    )


@app.route("/about.html")
def about_us():
    return render_template("about_page.html", page_title="Ferrari Car Deliveries")


@app.route("/landing")
def landing_page():
    return render_template("landing_page.html")


@app.route("/form-handling")
def formHandler():
    return render_template("form.html", page_title="Handling Form Submissions")
