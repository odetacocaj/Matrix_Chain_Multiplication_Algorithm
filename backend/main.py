# main.py
from flask import Flask, request, jsonify
from matrix_chain import compute_matrix_chain
from utils import format_optimal_order

app = Flask(__name__)

# Route to handle matrix chain multiplication
@app.route('/api/calculate', methods=['POST'])
def calculate():
    # Get the matrix dimensions from the request body
    data = request.get_json()
    num_matrices = data.get('num_matrices', 0)
    dimensions = data.get('dimensions', [])

    if num_matrices == 0 or not dimensions:
        return jsonify({'error': 'Invalid input, please provide num_matrices and dimensions.'}), 400

    # Calculate the optimal multiplication order
    costs, splits = compute_matrix_chain(dimensions)

    # Get the minimal number of scalar multiplications
    min_multiplications = costs[0][num_matrices - 1]

    # Get the optimal order of multiplication
    optimal_order = format_optimal_order(splits, 0, num_matrices - 1)

    # Return the results as JSON
    return jsonify({
        'min_multiplications': min_multiplications,
        'optimal_order': optimal_order
    })

if __name__ == '__main__':
    app.run(debug=True)
