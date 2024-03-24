from flask import Flask, url_for

app = Flask(__name__)


# HOME PAGE w/ link to ABOUT US / jinja template
@app.route('/')
@app.route('/home')
def homepage_url():
    about_us_url = url_for('about_us_url')
    return f"""
    <!doctype>
    <html>
        <head>
            <title>Plantify</title>
        </head>
        <body>
            <h1>Welcome to Plantify</h1>
            <p>Hello!</p>
            <hr>
            <a href="{about_us_url}">About Us</a>
        </body>
    </html> 
    """


#  ABOUT US PAGE w/ link to PRODUCT PAGE
@app.route('/about_us')
def about_us_url():
    product_page = url_for('product_url')
    return f"""
    <!doctype>
    <html>
        <head>
            <title>Plantify</title>
        </head>
        <body>
            <h1>About Plantify</h1>
            <p>
                We're an online shop for indoor plants. Checkout our plants below!
                <br>
                Subscribe to our mailing list to get tips and tricks to help your plants thrive indoors
            </p>
            <hr>
            <a href="{product_page}">Products</a>
        </body>
    </html> 
    """


@app.route('/product')  #use database. change to product/<plant_name> or <plant_ID>
def product_url():
    return "Product Page"



# RUN FLASK APP
if __name__ == "__main__":
    app.run(debug=True)