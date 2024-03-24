# import flask class and url_for function from flask library
from flask import Flask, url_for

# instantiate a Flask object (instance of Flask class)
# '__name__' is special variable giving Python files a unique name to correctly locate them
app = Flask(__name__)


# a get route by default, unless specified otherwise
@app.route('/')  # decorator that tells Flask which URL should trigger the function below
@app.route('/home')  # can have more than one decorator allowing function to be accessible from different url
def home_page():  # define function called when root or /home url is accessed
    # 'url_for()' dynamically builds urls for specific functions
    # takes name of function you want to generate an url for as an argument
    # avoids hard coding urls so if route is changed the urls don't need manually updating throughout app
    # 'url_for()' automatically generates correct url based on new route
    home_url = url_for('home_page')  # 'url_for()' dynamically generates url for home_page and stores in a variable
    about_url = url_for('about_page')  # generates url for about page
    portfolio_url = url_for('portfolio_page')  # generates url for portfolio page
    contact_url = url_for('contact_page')  # generates url for contact page

    # within this function, 'home_url = url_for('home_page')' generates an url path for the home_page function and ...
    # assigns it to the home_url variable. The url path corresponds to '@app.route('/')' or '@app.route(/home)' decorator
    # the variables are used to create hyperlinks (<a></a>) within the navigation section of each page
    # e.g. '{home_url}' is replaced with the generated url for the home page when Python code is executed

    # HTML string below is returned and rendered in the browser
    # f-string with triples quotes as it is multiline
    return f""" 
    <!doctype>
    <html>
        <head>
            <title>Home</title>
            <link rel="stylesheet" href="./static/styles.css">
        </head>
        <body>
            <nav>
                <a href="{home_url}">Home</a>
                <a href="{about_url}">About</a>
                <a href="{portfolio_url}">Portfolio</a>
                <a href="{contact_url}">Contact</a>
            </nav>
            <main>
            <h1>Home Page</h1>
            <section>
            <p>Welcome to my first Flask website!</p>
            </section>
            </main>
            <footer>&copy; Bek &amp; SKY Get Into Tech, 2024</footer>
        </body>
    </html>
    """


# structure is similar for about_page
# the decorator tells Flask the about url should trigger the function below
@app.route('/about')
def about_page():  # define the function for the about page
    home_url = url_for('home_page')  # identical to code in home_page function
    about_url = url_for('about_page')
    portfolio_url = url_for('portfolio_page')
    contact_url = url_for('contact_page')
    # HTML structure is the same with changes only to title and written content relevant to the page
    return f"""
    <!doctype>
    <html>
        <head>
            <title>About</title>
            <link rel="stylesheet" href="./static/styles.css">
        </head>
        <body>
            <nav>
                <a href="{home_url}">Home</a>
                <a href="{about_url}">About</a>
                <a href="{portfolio_url}">Portfolio</a>
                <a href="{contact_url}">Contact</a>
            </nav>
            <main>
            <h1>About Page</h1>
            <section>
            <p>This is a very simple Flask website to learn about using html routes and anchor tags for navigating between pages.</p>
            <p>It's not pretty and it's really not practical (lots of duplicated code).</p>
            <p>To be continued...</p>
            </section>
            </main>
            <footer>&copy; Bek &amp; SKY Get Into Tech, 2024</footer>
        </body>
    </html>     
    """


# repeat the structure for portfolio_page
@app.route('/portfolio')
def portfolio_page():
    home_url = url_for('home_page')
    about_url = url_for('about_page')
    portfolio_url = url_for('portfolio_page')
    contact_url = url_for('contact_page')
    return f"""
    <!doctype>
    <html>
        <head>
            <title>Portfolio</title>
            <link rel="stylesheet" href="./static/styles.css">
        </head>
        <body>
            <nav>
                <a href="{home_url}">Home</a>
                <a href="{about_url}">About</a>
                <a href="{portfolio_url}">Portfolio</a>
                <a href="{contact_url}">Contact</a>
            </nav>
            <main>
            <h1>Portfolio Page</h1>
            <section>
            <p>Projects...</p>
            </section>
            </main>
            <footer>&copy; Bek &amp; SKY Get Into Tech, 2024</footer>
        </body>
    </html>
    """


# repeat the structure for contact_page
@app.route('/contact')
def contact_page():
    home_url = url_for('home_page')
    about_url = url_for('about_page')
    portfolio_url = url_for('portfolio_page')
    contact_url = url_for('contact_page')
    return f"""
    <!doctype>
    <html>
        <head>
            <title>Contact</title>
            <link rel="stylesheet" href="./static/styles.css">
        </head>
        <body>
            <nav>
                <a href="{home_url}">Home</a>
                <a href="{about_url}">About</a>
                <a href="{portfolio_url}">Portfolio</a>
                <a href="{contact_url}">Contact</a>
            </nav>
            <main>
            <h1>Contact Page</h1>
            <section>
            <p>Contact me...</p>
            </section>
            </main>
            <footer>&copy; Bek &amp; SKY Get Into Tech, 2024</footer>
        </body>
    </html>     
    """


# '__name__' is special built-in variable and when script is executed Python sets '__name__' variable to '"__main__"' if script is being run as main program
# if script is imported as a module into another script then '__name__' is set to the script/module name
# first line checks if script is being run directly by the Python interpreter and condition is true if the script is executed as the main program/entry point of app
if __name__ == "__main__":
    # app object is instance of the Flask class, run tells Flask to start serving application to handle incoming web requests
    # 'debug=True' argument enables debug mode within the Flask application
    # - automatically reloads Flask application if you make changes to the code
    # - interactive debugger shown in the web browser
    app.run(debug=True)


# # ////// LESSON CODE //////
# @app.route('/page1/<name>')
# def simple_html_page(name):
#     # url_for() is a flask method to get url python function
#     home_url = url_for('hello_from_flask')
#     return f"""
#     <!doctype>
#     <html>
#         <head>
#             <title>Page 1</title>
#         </head>
#         <body>
#             <h1>Name Page</h1>
#             <p>Hello {name}!</p>
#             <hr>
#             <a href="{home_url}">Home Page</a>
#         </body>
#     </html>
#     """

# # a get route by default
# @app.route('/bye')
# def goodbye_from_flask():
#     return "Goodbye from Flask :("
#
#
# # brackets means replaceable parameter
# @app.route('/dynamic/<colour>')
# def echo_colour_choice(colour):
#     return f"You like the colour {colour}"
#
#
# @app.route('/dynamicname/<name>')
# def hello_name(name):
#     return f"Hello {name}"
#
#
# @app.route('/square/<int:number>')
# def square(number):
#     squared = number ** 2
#     message = "Your number squared is " + str(squared)
#     return message
