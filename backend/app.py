from flask import Flask, request, jsonify
from matrix_chain import compute_matrix_chain
from utils import format_optimal_order
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS to allow cross-origin requests from React frontend on port 5173
CORS(app, origins="http://localhost:5173")  # Adjusting the allowed origin

@app.route('/matrix-chain', methods=['POST'])
def matrix_chain():
    # Get the input dimensions from the POST request
    data = request.get_json()
    dimensions = data['dimensions']

    # Compute the matrix chain multiplication
    costs, splits = compute_matrix_chain(dimensions)

    # Get the optimal multiplication order
    optimal_order = format_optimal_order(splits, 1, len(dimensions) - 1)

    # Prepare the result to send back
    result = {
        "min_cost": costs[1][len(dimensions) - 1],
        "optimal_order": optimal_order
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
