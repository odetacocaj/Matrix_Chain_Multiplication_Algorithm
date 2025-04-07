import React, { useState } from "react";
import axios from "axios";
import "./App.css";

const MatrixChain = () => {
  const [numMatrices, setNumMatrices] = useState(0);
  const [dimensions, setDimensions] = useState([]);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleMatrixChange = (index, value) => {
    const newDimensions = [...dimensions];
    newDimensions[index] = parseInt(value);
    setDimensions(newDimensions);
  };

  const handleSubmit = async () => {
    setLoading(true);
    try {
      const response = await axios.post("http://127.0.0.1:5000/matrix-chain", {
        dimensions: dimensions,
      });
      setResult(response.data);
    } catch (error) {
      console.error("Error:", error);
    }
    setLoading(false);
  };

  return (
    <>
      <h1>Matrix Chain Multiplication</h1>
      <div className="matrix-chain-container">
        <div className="input-container">
          <label>
            Number of Matrices:
            <input
              type="number"
              value={numMatrices}
              onChange={(e) => setNumMatrices(parseInt(e.target.value))}
              min="1"
            />
          </label>

          {/* Render the matrix inputs only if numMatrices is greater than 0 */}
          {numMatrices > 0 &&
            Array.from({ length: numMatrices }).map((_, index) => (
              <div key={index} className="matrix-input">
                <label>
                  Matrix {index + 1} Rows:
                  <input
                    type="number"
                    value={dimensions[index] || ""}
                    onChange={(e) => handleMatrixChange(index, e.target.value)}
                    min="1"
                  />
                </label>
              </div>
            ))}

          {/* Render the columns input only after number of matrices is entered */}
          {numMatrices > 0 && (
            <div className="matrix-input">
              <label>
                Matrix {numMatrices} Columns:
                <input
                  type="number"
                  value={dimensions[numMatrices] || ""}
                  onChange={(e) => handleMatrixChange(numMatrices, e.target.value)}
                  min="1"
                />
              </label>
            </div>
          )}

          <button className="submit-btn" onClick={handleSubmit} disabled={loading}>
            {loading ? "Processing..." : "Submit"}
          </button>
        </div>

        {result && (
          <div className="result-container">
            <h2>Results:</h2>
            <p>
              <strong>Minimal Scalar Multiplications:</strong> {result.min_cost}
            </p>
            <p>
              <strong>Optimal Order:</strong> {result.optimal_order}
            </p>
          </div>
        )}
      </div>
    </>
  );
};

export default MatrixChain;
