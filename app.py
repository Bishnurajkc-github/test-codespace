from flask import Flask

app = Flask(__name__)

# This is HOME ROute

@app.route("/")
def home():
    return "<h1>Hello from Codespaces!</h1>"

# THis is About Route

@app.route("/about")
def about():
    return "<h2>This is the about page</h2>"

if __name__ == "__main__":
    app.run(debug=True)