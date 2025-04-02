def format_optimal_order(splits, start, end):
    """
    Ndërton si string paraqitjen optimale të renditjes së shumëzimit.
    """
    if start == end:
        return f"A{start}"
    
    split = splits[start][end]
    left_part = format_optimal_order(splits, start, split)
    right_part = format_optimal_order(splits, split + 1, end)
    
    return f"({left_part} x {right_part})"
