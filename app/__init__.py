from flask import Flask, jsonify, request
import logging
from .database import session_instance

app = Flask(__name__)

# Create a logger instance specific to the current module
logger = logging.getLogger(__name__)

# Define a log formatter with a specific format
log_formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(name)s %(message)s"
)

# Set the logging level for the logger to capture messages of severity ERROR and above
logger.setLevel(logging.INFO)


@app.route('/ping')
def ping():
    return jsonify({'message': 'pong'})


@app.route('/recommend/<str:isbn>', methods=['GET'])
def recommend_books(isbn):
    try:
        pass
    except Exception as e:
       pass