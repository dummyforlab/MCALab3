def diff_ways_to_evaluate(expression, memo={}):
    if expression in memo:
        return memo[expression]

    # If the expression is a pure number, just return it
    if expression.isdigit():
        return [int(expression)]

    results = []

    for i, char in enumerate(expression):
        if char in '+-*':
            # Split expression at operator
            left_expr = expression[:i]
            right_expr = expression[i+1:]

            # Recursively evaluate all possibilities for left and right
            left_results = diff_ways_to_evaluate(left_expr, memo)
            right_results = diff_ways_to_evaluate(right_expr, memo)

            # Combine results based on operator
            for left in left_results:
                for right in right_results:
                    if char == '+':
                        results.append(left + right)
                    elif char == '-':
                        results.append(left - right)
                    elif char == '*':
                        results.append(left * right)

    memo[expression] = results
    return results

def min_result(expression):
    results = diff_ways_to_evaluate(expression)
    return min(results)

# Example usage
expr = "2*3-4*5"
print("Minimum result:", min_result(expr))  # Output: -34
