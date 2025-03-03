from flask import Flask, render_template

app = Flask(__name__)

pages = []

pages.append(
    {
        "page_title": "Welcome",
        "page_header": "Welcome to My Website",
        "page_content": "This is my first dynamic website.",
    }
)

pages.append(
    {
        "page_title": "About Us",
        "page_header": "About This Website",
        "page_content": "This is a dynamic website built using Python.",
    }
)

pages.append(
    {
        "page_title": "Contact Us",
        "page_header": "How to Get in Touch",
        "page_content": "We're always happy to hear from you.",
    }
)

products = [
    {
        "name": "Mars",
        "price": "700CFA",
        "description": "Delicious chocolate bar",
        "url": "mars-bar",
    },
    {
        "name": "Snickers",
        "price": "700CFA",
        "description": "Delicious chocolate and peanut bar",
        "url": "snickers-bar",
    },
    {
        "name": "KitKat",
        "price": "700CFA",
        "description": "Easy to share chocolate covered biscuit",
        "url": "kitkat",
    },
]


@app.route("/")
@app.route("/<int:page_id>")
@app.route("/<int:page_id>/<string:friendly_name>")
def home(page_id=0, friendly_name=""):
    print("Loading Page", pages[page_id])
    page_title, page_header, page_content = pages[page_id].values()

    return render_template(
        "default.html",
        page_title=page_title,
        page_header=page_header,
        page_content=page_content,
    )


@app.route("/products")
def products_page():
    return render_template("listings.html", products=products)


@app.route("/product/<int:product_id>/<string:product_url>")
def product_details_page(product_id, product_url):
    product_index = product_id - 1
    product = products[product_index]
    return render_template("details.html", product=product)


if __name__ == "__main__":
    app.run(debug=True)
