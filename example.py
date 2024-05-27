from generator import generate_constants
from model import model_operation
from result import compare_results, save_results_to_file


def example_run():
    seed = 12345
    constants = generate_constants(seed)
    inputs = [(constants['a'], constants['b']), (constants['b'], constants['c'])]

    operation = '+'
    model_results = model_operation(inputs, operation)

    user_results = [constants['a'] + constants['b'], constants['b'] + constants['c']]
    comparison_results = compare_results(user_results, model_results)

    save_results_to_file('results.txt', user_results, model_results, comparison_results)
    print(f"User Results: {user_results}")
    print(f"Model Results: {model_results}")
    print(f"Comparison: {comparison_results}")


if __name__ == '__main__':
    example_run()
