from flask import Flask, url_for

app = Flask(__name__)


# HOME PAGE w/ link to ABOUT US / jinja template
@app.route('/')
@app.route('/home')
def homepage_url():     #FUNCTIONS TO ROUTE TO OTHER PAGES. LINKS EMBEDDED IN THE TEXT BELOW
    about_us = url_for('about_us_url')
    collection = url_for('collection_url')
    subscribe = url_for('subscribe_url')
    login = url_for('customer_login_url')
    admin = url_for('admin_login_url')
    return f"""
    <!doctype>
    <html>
        <head>
            <title>Plantify</title>
        </head>
        <body>
            <h1>Welcome to Plantify</h1>
            <h3>We're on a mission to fill homes with plants.</h3>
            <h4>Subscribe to the mailing list to receive weekly tips and tricks to keep your plants thriving indoors.</h4>
            <hr>
            <h2>
                Menu
            </h2>
                <b>Home</b>
                <a href="{about_us}">About Us</a>
                <a href="{collection}">Plant Collection</a>
                <a href="{subscribe}">Subscribe</a>
                <a href="{login}">Login</a>
                <a href="{admin}">Administrator Login</a>
            <hr>
            <h8>
                copyright Plantify ltd
            </h8>
        </body>
    </html> 
    """


#  ABOUT US PAGE W/ LINKS
@app.route('/about_us')
def about_us_url():
    home_page = url_for('homepage_url')
    collection = url_for('collection_url')
    subscribe = url_for('subscribe_url')
    login = url_for('customer_login_url')
    admin = url_for('admin_login_url')
    return f"""
    <!doctype>
    <html>
        <head>
            <title>About Us</title>
        </head>
        <body>
            <h1>
                Plantify
            </h1>
            
            <h2>
                About Us
            </h2>
            
            <p>
                We're an online shop for indoor plants. Checkout our
                    <a href="{collection}">plant collection.</a>
                <br>
                Subscribe to our mailing list to get tips and tricks to help your plants thrive indoors.
            </p>
            <hr>
            <h2>
                Menu
            </h2>
                <a href="{home_page}">Home</a>
                <b>About Us</b>
                <a href="{collection}">Plant Collection</a>
                <a href="{subscribe}">Subscribe</a>
                <a href="{login}">Login</a>
                <a href="{admin}">Administrator Login</a>
            <hr>
            <h8>
                copyright Plantify ltd
            </h8>
        </body>
    </html> 
    """


#SUGGESTION: USE DATABASE. COLUMNS: PRODUCT ID, PRODUCT NAME, DESCRIPTION, PRICE. HAVE A BUTTON TO ADD TO BASKET. BASKET IS A NEW PAGE WHICH WILL ADD ITEMS WITHIN
@app.route('/collection')
def collection_url():
    home_page = url_for('homepage_url')
    about_us = url_for('about_us_url')
    subscribe = url_for('subscribe_url')
    login = url_for('customer_login_url')
    admin = url_for('admin_login_url')
    return f"""
    <!doctype>
    <html>
        <head>
            <title>Collection</title>
        </head>
        <body>
            <h1>
                Plantify
            </h1>
            <h2>
                Our Collection
            </h2>
            <p>
                Shop our collection and 
                    <a href="{subscribe}">subscribe </a>
                to our mailing list for tips to help your plant flourishing indoors.
                <br>
                <br>
            </p>
            
            <h3>
                AGLAONEMA PINK STAR
            </h3>
            <p>
                The Aglaonema Pink Star is a gorgeous rare plant that will thrive easily in your home. Tolerant of low light conditions and easy care, they are perfect plants for the beginner but attractive collector plants for more experienced growers.
            </p>
                <br>
            <h3>
                EPIPREMNUM AUREUM (DEVILS IVY, GOLDEN POTHOS)
            </h3>
            <p>
                Pothos Plants, or Epipremnum Aureum, are native to the jungles of Malaysia and are highly adaptable, glossy-leafed plants with heart-shaped leaves. Epipremnum Aureum or devils Ivy is easy to care for and can grow almost anywhere. In other words, a perfect houseplant for beginners.
            </p>
                <br>
                      
            <hr>
            <h2>
                Menu
            </h2>
                <a href="{home_page}">Home</a>
                <a href="{about_us}">About Us</a>
                <b>Collection</b>
                <a href="{subscribe}">Subscribe</a>
                <a href="{login}">Login</a>
                <a href="{admin}">Administrator Login</a>
            <hr>
            <h8>
                copyright Plantify ltd
            </h8>
        </body>
    </html> 
    """

# SUGGESTION: ADD A TABLE TO ALLOW A POST REQUEST INTO A DATABASE. COLUMNS: PERSON ID, FIRST NAME, LAST NAME AND EMAIL, PASSWORD
# SUBSCRIBE PAGE
@app.route('/subscribe') #ROUTE TO SUBSCRIBE PAGE
def subscribe_url():
    home_page = url_for('homepage_url')
    about_us = url_for('about_us_url')
    collection = url_for('collection_url')
    login = url_for('customer_login_url')
    admin = url_for('admin_login_url')
    return f"""
        <!doctype>
        <html>
            <head>
                <title>Subscribe</title>
            </head>
            <body>
                <h1>
                    Plantify
                </h1>

                <h2>
                    Subscribe to the Mailing List
                </h2>

                <p>
                    We're an online shop for indoor plants. Checkout our
                        <a href="{collection}">plant collection.</a>
                    <br>
                    Email plantify@yopmail.co.uk to subscribe to our mailing list to get tips and tricks to help your plants thrive indoors. Send your full name and email address.
                </p>
                <hr>
                <h2>
                    Menu
                </h2>
                    <a href="{home_page}">Home</a>
                    <a href="{about_us}">about_us_url</a>
                    <a href="{collection}">Plant Collection</a>
                    <b>Subscribe</b>
                    <a href="{login}">Login</a>
                    <a href="{admin}">Administrator Login</a>
                <hr>
                <h8>
                    copyright Plantify ltd
                </h8>
            </body>
        </html> 
        """


# SUGGESTION: INTEGRATED INTO A DATABASE TO CHECK CREDENTIALS (USERNAME = EMAIL, PASSWORD)
@app.route('/login') #ROUTE TO CUSTOMER LOGIN PAGE
def customer_login_url():
    home_page = url_for('homepage_url')
    about_us = url_for('about_us_url')
    collection = url_for('collection_url')
    subscribe = url_for('subscribe_url')
    admin = url_for('admin_login_url')
    return f"""
        <!doctype>
        <html>
            <head>
                <title>Login</title>
            </head>
            <body>
                <h1>
                    Plantify
                </h1>

                <h2>
                    Log Into Your Account
                </h2>

                <p>
                    Enter your login details:
                    <br>
                    Not a member? Create your free account 
                    <a href="{subscribe}">here.</a>
                </p>
                <hr>
                <h2>
                    Menu
                </h2>
                    <a href="{home_page}">Home</a>
                    <a href="{about_us}">about_us_url</a>
                    <a href="{collection}">Plant Collection</a>
                    <a href="{subscribe}">Subscribe</a>
                    <b>Login</b>
                    <a href="{admin}">Administrator Login</a>
                <hr>
                <h8>
                    copyright Plantify ltd
                </h8>
            </body>
        </html> 
        """


# SUGGESTION: INTEGRATE TO AN ADMINISTRATOR DATABASE. COLUMNS: PERSON ID, FIRST NAME, LAST NAME, EMAIL ADDRESS PASSWORD
@app.route('/admin') #ROUTE TO CUSTOMER LOGIN PAGE
def admin_login_url():
    home_page = url_for('homepage_url')
    about_us = url_for('about_us_url')
    collection = url_for('collection_url')
    subscribe = url_for('subscribe_url')
    login = url_for('customer_login_url')
    return f"""
        <!doctype>
        <html>
            <head>
                <title>Administrator Login</title>
            </head>
            <body>
                <h1>
                    Plantify
                </h1>

                <h2>
                    Log Into Your Account
                </h2>

                <p>
                    Enter your Administrator login details:
                    <br>
                </p>
                <hr>
                <h2>
                    Menu
                </h2>
                    <a href="{home_page}">Home</a>
                    <a href="{about_us}">about_us_url</a>
                    <a href="{collection}">Plant Collection</a>
                    <a href="{subscribe}">Subscribe</a>
                    <a href="{login}">Log in</a>
                    <b>Administrator Login</b>
                <hr>
                <h8>
                    copyright Plantify ltd
                </h8>
            </body>
        </html> 
        """



# RUN FLASK APP
if __name__ == "__main__":
    app.run(debug=True)