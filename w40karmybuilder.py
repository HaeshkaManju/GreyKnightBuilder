from flask import Flask, render_template
app = Flask(__name__)

# This file is part of the render(ing) domain.
# Once this file is established, tested and proven to function, as intended - do not modify the existing code, only extend from it.

## use decorates for handling the URL structure.  Do not hard-code URL structure with HTML files.

## format:
## @app.route("/[urlname]")
## def urlname():
##      return render_template('urlname.html', other variables.)
### additional arguments should be ordered as follows:
### Page Title, Header Tags (if applicable), Block Content, Block Content Variables, form content, form content submission options.

# Self Note: two decorators directly following allows setting the same define function to the same route.
# @app.route("/")
# @app.route("/home")
# def home():
#    return render_template('home.html')

@app.route("/display_unit.html")
def display_unit():
    return render_template('display_unit.html')

### For the love of all that is holy - do not run this block in a production environment. ###
if __name__ == '__main__':
    app.run(debug=True)
# comment-out the above block when in production.
# Above block to be used in test environment.
# run flask server startup direct from command line in production environment.
