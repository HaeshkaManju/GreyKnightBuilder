from flask import Flask, render_template

# This is not an actual, operational file.
# This file is solely here as a blueprint to remind that all variables and data
## need to be pushed through flask and its render.

print(""" <html>
<head>
	<title>Attempt with Python</title>
</head>
<body>
	<h1>Non-Pythonic</h1>
	{% variable %}
	{{ variable }}
</body>
</html>""")


## likely variables and data.

unitdata = [] # replace with a method from the class.unit.py file.
## Expressly asks for all of the unit's data, to be dumped into a single array.

page_name = ''
page_title = '' # Use a Standard:
## Home
## Unit: Unit Name
## Army List: Army Name
## Edit Army: Army Name
### Format should be 'Home' + page_name

logged_in = # booleanself.
