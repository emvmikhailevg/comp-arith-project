def arithmetic_operation(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b if b != 0 else None
    else:
        raise ValueError("Invalid operation")


def model_operation(inputs, operation):
    result = []
    for pair in inputs:
        res = arithmetic_operation(pair[0], pair[1], operation)
        if res is not None:
            result.append(res)
    return result
