from flask import Flask
from metro.logger import logging

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    logging.info("We are testing module")
    return "Starting ml projects"


if __name__ == "__main__":
    app.run(debug=True)
