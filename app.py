from flask import Flask

app = Flask(__name__)


# HOME ROUTE
@app.route("/")
def home():
    return """
    <h1>Welcome to My Mini Blog 🚀</h1>
    <p>This is the home page running on Flask.</p>
    <a href="/about">Go to About</a>
    """


# ABOUT ROUTE
@app.route("/about")
def about():
    return """
    <h2>About Page</h2>
    <p>This Flask app is running from my PC and synced with GitHub.</p>
    <a href="/">Back to Home</a>
    """


if __name__ == "__main__":
    app.run(debug=True)
