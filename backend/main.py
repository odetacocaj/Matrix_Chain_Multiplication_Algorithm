from flask import Flask, request, jsonify
from matrix_chain import compute_matrix_chain
from utils import format_optimal_order
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins="http://localhost:5173")  

@app.route('/matrix-chain', methods=['POST'])
def matrix_chain():
    data = request.get_json()
    dimensions = data.get('dimensions', [])

    # Validate that the input is not empty and contains at least two dimensions
    if not dimensions or len(dimensions) == 1:
        return jsonify({'error': 'Invalid input, please provide valid dimensions.'}), 400

    # Check if any dimension is negative
    if any(d <= 0 for d in dimensions):  
        return jsonify({'error': 'Invalid input, dimensions must be positive numbers.'}), 400

    if len(dimensions) == 3:
        min_cost = dimensions[0] * dimensions[1] * dimensions[2]
        return jsonify({'min_cost': min_cost, 'optimal_order': '(A1 x A2)'})

    costs, splits = compute_matrix_chain(dimensions)

    optimal_order = format_optimal_order(splits, 1, len(dimensions) - 1)

    result = {
        "min_cost": costs[1][len(dimensions) - 1],
        "optimal_order": optimal_order
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
