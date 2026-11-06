from flask import Flask, request, render_template_string

app= Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome! Flask</h1>"


if __name__=="__main__":
    app.run(debug=True)
