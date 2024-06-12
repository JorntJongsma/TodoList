from flask import Flask

app = Flask(__name__)

@app.route("/")
def mainPage():
    return "<p> this is the main page </p>"

if __name__ == "__main__":
    app.run("192.168.178.220",5000, debug=True)