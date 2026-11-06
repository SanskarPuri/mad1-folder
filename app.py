from flask import Flask, render_template_string, request

app=Flask(__name__)

""" Now we can make our routes
    to make routes we use @app.route("/write path")
"""

@app.route("/")
def home():
    return "<h1><i>Hello I am using flask.</i></h1>"

@app.route("/about/<name>")
def about_route(name):
    content = """<!DOCTYPE html>
            <html>
                <head>
                    <title>Description</title>
                </head>
                <body>
                    <h1>Hello! {{ name }} We are using flask</h1>
                    <p>flask is used to make web applications. Its a micro framework we can use it to make small applications. To see more on it <br><a href="https://www.geeksforgeeks.org/python/flask-tutorial/" target="_blank">Know more<a>
                    </p>
                </body>
            </html>"""
    return render_template_string(content, name=name)
@app.route("/user/<name>")
def users(name):
    return f"<h1><i>Welcome again @{name}__</i></h1>"

#Multiple parameters
@app.route("/students/<name>/<course>")
def studentsinfo(name,course):
    return f"<h1>{name} is studying {course} at IIT Madras.</h1>"

# Query parameters are parts of URL that follows a question marks and key value pair
@app.route("/query")
def query_params():
    name= request.args.get("name","default value")
    return f"<h1>Searched results for your query {name}</h1>"
if __name__=="__main__":
    app.run(debug=True)
