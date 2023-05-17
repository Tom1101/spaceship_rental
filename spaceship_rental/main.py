from flask import Flask, request, jsonify
from spaceship_rental.contracts import optimize_spaceship
import logging.config

app = Flask(__name__)

# Load the logger configuration from the file
logging.config.fileConfig('./logging_config.ini')

# Get the logger instance
logger = logging.getLogger(__name__)


@app.route('/spaceship/optimize', methods=['POST'])
def spaceship_optimize():
    try:
        contracts = request.get_json()
        result = optimize_spaceship(contracts, logger)
        logger.info(f"Optimization result: {result}")

        return jsonify(result)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500


def webserver():
    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    webserver()
