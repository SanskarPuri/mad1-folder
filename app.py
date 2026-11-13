from flask import Flask, request, render_template

app= Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome! Flask</h1>"

@app.route("/submit-form", methods=['GET', 'POST'])
def get_form_data():
    if request.method=='POST':
        name=request.form.get("username")
        email=request.form.get("useremail")
        password=request.form.get("userpass")

        print("\n=== NEW FORM SUBMISSION ===")
        print(f"Name entered:     {name}")
        print(f"Email entered:    {email}")
        print(f"Password entered: {password}")
        print("===========================\n")

        return f"<h1> Thankyou for submitting the form! {name}"
    return render_template('index.html')

@app.route("/users")
def user_details():
    users={
            "user1": [
        "Alex Mercer",                    # Name
        "alex.mercer@example.com",        # Email
        ["Hello World!", "Flask is fun"], # Posts (List of strings)
        142                               # Likes (Integer)
    ],
    "user2": [
        "Jane Doe",
        "jane.doe@example.com",
        ["My first post", "Travel blog"],
        389
    ],
    "user3": [
        "Sam Wilson",
        "sam.w@example.com",
        ["Chilling at home", "Coding all night!"],
        54
    ]
    }
    top_user_list=max(users.values(), key=lambda u: u[3])
    highest={
            "name": top_user_list[0],
            "likes": top_user_list[3]
            }

    return render_template("jinja.html", users=users, top_user=highest)

#Accessing the home, contact and about route from templates to test the working of extends.

@app.route("/home")
def home_route():
    return render_template("home.html")

@app.route("/about")
def about_route():
    return render_template("about.html")

@app.route("/contact")
def contact_route():
    return render_template("contact.html")


if __name__=="__main__":
    app.run(debug=True, port=8080)
