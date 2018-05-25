def permutations(a):
    permutations = []
    list_iterator(permutations, a, [], len(a), False, False)
    return permutations

def combinations(a, k, repeat=False):
    combinations = []
    list_iterator(combinations, a, [], k, repeat, True)
    return combinations

def variations(a, k, repeat=False):
    variations = []
    list_iterator(variations, a, [], k, repeat, False)
    return variations

def list_iterator(result, left, actual, k, repeat, is_combination):

    if k == 0:
        result.append(actual)
        return

    for element in list(left):

        new_left = list(left)
        if not repeat:
            new_left.remove(element)

        new_actual = list(actual)
        new_actual.append(element)

        list_iterator(result, new_left, new_actual,
                       k - 1, repeat, is_combination)

        if is_combination:
            left.remove(element)
