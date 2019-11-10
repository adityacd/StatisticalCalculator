from Calculator.Addition import addition


def proportion(numbers):
    proportion_list = []
    for g in numbers:
        h = g / addition(numbers)
        proportion_list.append(h)
    return proportion_list
