from flask import Flask, render_template, Blueprint
from routes import my_blueprint

app = Flask(__name__)

if __name__ == "__main__":
    app.register_blueprint(my_blueprint)
    app.run(debug=True)
