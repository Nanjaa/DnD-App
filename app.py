from flask import Flask
from campaigns import campaigns_api


app = Flask(__name__)


app.register_blueprint(campaigns_api, url_prefix='/campaigns')


if __name__ == '__main__':
    app.run(debug=True)