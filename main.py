from matrix_chain import compute_matrix_chain
from utils import format_optimal_order

# Marrja e të dhënave nga përdoruesi
num_matrices = int(input("Jepni numrin e matricave: "))
dimensions = []
for i in range(num_matrices):
    row_count = int(input(f"Jepni numrin e rreshtave për matricën {i + 1}: "))
    dimensions.append(row_count)
dimensions.append(int(input(f"Jepni numrin e kolonave për matricën {num_matrices}: ")))

# Llogarit renditjen optimale të shumëzimit
costs, splits = compute_matrix_chain(dimensions)

# Shfaqja e rezultateve
print(f"Numri minimal i shumëzimeve skalar: {costs[1][num_matrices]}")
print(f"Parentesizimi optimal: {format_optimal_order(splits, 1, num_matrices)}")
