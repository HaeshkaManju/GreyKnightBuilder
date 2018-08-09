from flask import Flask, render_template
app = Flask(__name__)

# This file is part of the render(ing) domainself.
# Once this file is established, tested and proven to function, as intended - do not modify the existing code, only extend from it.

## use decorates for handling the URL structure.  Do not hard-code URL structure with HTML files.

## format:
## @app.route("/[urlname]")
## def urlname():
##      return render_template('urlname.html', other variables.)
### additional arguments should be ordered as follows:
### Page Title, Header Tags (if applicable), Block Content, Block Content Variables, form content, form content submission options.

# Self Note: two decorators directly following allows setting the same define function to the same route.
if logged_in = True:
    @app.route("/")
    @app.route("/home")
    def home():
        return render_template('dashboard.html', title=home_title, dashboard_block=True, sign_up_block=False, login_block=False, logout_block=True)
else:
    @app.route("/")
    @app.route("/home")
    def home():
        return render_template('home.html', title=home_title, dashboard_block=False, sign_up_block=True, login_block=True, logout_block=False)

if logged_in = True:
    @app.route("/view_unit.html")
    def view_unit():
        return render_template('view_unit.html', title=view_unit, logout_block=False)
else:
    @app.route("/home")
    def home():
        return render_template('home.html', title=home_title, dashboard_block=False, sign_up_block=True, login_block=True)


### For the love of all that is holy - do not run this block in a production environment. ###
if__name__== '__main__':
    app.run(debug=True)
# comment-out the above block when in production.
# Above block to be used in test environment.
# run flask server startup direct from command line in production environment.
