def compute_matrix_chain(dimensions):
    """
    Llogarit numrin minimal të shumëzimeve skalar për shumëzimin e zinxhirit të matricave.
    
    Argumentet:
        dimensions (list): Listë ku matrica Ai ka dimensione dimensions[i-1] x dimensions[i].
    
    Kthen:
        tuple: Një tuple (costs, splits) ku:
            - costs[i][j] përmban koston minimale për shumëzimin e Ai...Aj.
            - splits[i][j] ruan indeksin optimal të ndarjes.
    """
    num_matrices = len(dimensions) - 1  # Sepse lista dimensions ka një vlerë shtesë
    costs = [[0] * (num_matrices + 1) for _ in range(num_matrices + 1)]
    splits = [[0] * (num_matrices + 1) for _ in range(num_matrices + 1)]
    
    for chain_len in range(2, num_matrices + 1):  # Fillimi i gjatësise së zinxhirit
        for start in range(1, num_matrices - chain_len + 2):
            end = start + chain_len - 1
            costs[start][end] = float('inf')
            
            for split in range(start, end):
                cost = (
                    costs[start][split] + costs[split + 1][end] +
                    dimensions[start - 1] * dimensions[split] * dimensions[end]
                )
                
                if cost < costs[start][end]:
                    costs[start][end] = cost
                    splits[start][end] = split
    
    return costs, splits
