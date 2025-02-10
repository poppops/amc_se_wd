from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Tell the application where to store uploaded files
# We created a folder called uploads but you can name it as you like
app.config["UPLOAD_FOLDER"] = "uploads"


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


@app.route("/file-uploading", methods=["GET", "POST"])
def fileUploading():
    if request.method == "POST":
        print(request.form)
        print(request.files)

        # Assign the uploaded file to a variable
        profile_pic = request.files["profile_photo"]
        # Save the file on the file system (in our uploads folder)
        profile_pic.save(
            os.path.join(app.config["UPLOAD_FOLDER"], profile_pic.filename)
        )

    # Pass the file name into the template to display to the user
    return render_template("file_upload.html", uploaded_file=profile_pic.filename)
