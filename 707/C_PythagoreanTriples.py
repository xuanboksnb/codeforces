"""

"""
import math


def fact_monster_prime_numbers(number):
    square_root_value = int(math.sqrt(number))
    facts = dict()
    phan_thua = number
    i = 2
    while i <= square_root_value and i <= phan_thua:
        print i, phan_thua
        if phan_thua % i == 0:
            if i in facts:
                facts[i] += 1
            else:
                facts[i] = 1
            phan_thua = phan_thua / i
        else:
            i += 1
    return facts


def get_all_sub_sets(set_parent):
    """

    :param dict set_parent:
    :return:
    """
    if len(set_parent) == 0:
        return [dict()]
    else:
        current = set_parent.keys()[0]
        value = set_parent[current]
        del set_parent[current]
        print set_parent
        sub_other = get_all_sub_sets(set_parent)
        result = []
        # if len(sub_other) == 0:
        #     result.append([current])
        print sub_other
        for sub in sub_other:
            for i in range(value + 1):
                d = dict(sub)
                d[current] = i
                result.append(d)
        return result


# def get_pair_factor(number):
#     factors = fact_monster_prime_numbers(number)
#     result = set()
#     keys_sorted = sorted(factors.keys())
#     s = set()
#
#     for key in factors.keys():
#         for i in range(factors[key] + 1):
#             current_value *= key
#
#     pass



def get_pythagorean_triples(one_elememt):
    # for i in range(1,
    factors = fact_monster_prime_numbers(one_elememt)
    odd_value = [key for key in factors.keys() if key % 2 == 1]
    even_value = [key for key in factors.keys() if key % 2 == 0]
    current_value = 1

    all_sub_set_keys = get_all_sub_sets(factors)
    for sub in all_sub_set_keys:
        s = 1
        for prime in sub:
            for i in range(1, factors[prime] + 1):
                pass

    for key in factors.keys():
        for i in range(1, factors[key] + 1):
            current_value *= key

    pass


if __name__ == '__main__':
    # fact_monster_prime_numbers(30)
    print get_all_sub_sets({1:2, 2:4, 3:1})