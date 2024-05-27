def compare_results(user_results, model_results):
    return ["Верно" if u == m else "Неверно" for u, m in zip(user_results, model_results)]


def save_results_to_file(filename, user_results, model_results, comparison_results):
    with open(filename, 'w') as file:
        file.write("User Results: {}\n".format(user_results))
        file.write("Model Results: {}\n".format(model_results))
        file.write("Comparison: {}\n".format(comparison_results))
        