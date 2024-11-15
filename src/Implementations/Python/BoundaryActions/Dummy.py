from random import choice


def v1_dummy_boundary(state, params, spaces):
    return [{"string": choice(["A", "B", "C"])}]


def v1_dummy_boundary2(state, params, spaces):
    first = choice(["A", "B", "C"])
    second = choice(["A", "B", "C"])
    return [{"string": first + second}]


def v2_dummy_boundary2(state, params, spaces):
    first = choice(["A", "B", "C"])
    second = choice([x for x in ["A", "B", "C"] if x != first])
    return [{"string": first + second}]
