# Title: Bite 371. Combining dictionaries

"""
Bite 371. Combining dictionaries
"""

def combine_and_count(a: dict, b: dict) -> dict:
    """Combine two dictionaries.

    Return  new dictionary with the combined keys and values.
    For any key found in both dictionaries,
    return the sum of the values for that key.

    Args:
      a: The first dictionary.
      b: The second dictionary.

    Returns:
      A dictionary with the contents of both.
      Values of any shared keys are summed.
    """
    result = {}
    if not a and b:
        result = b
    if not b and a:
        result = a
    try:
        if common_keys := set(a.keys()) & set(b.keys()):
            result = {key: a[key] + b[key] for key in common_keys}
    except (TypeError,AttributeError) as e:
        raise TypeError() from e
    final_val = a | b
    final_val |= result
    return final_val

bad_fruit = {"orange": "two", "durian": 1}  # value you can't add
not_a_dict = "What am I, chopped liver?"  #


def test_bad_union() -> None:
    """Trying to combine the uncombinable raises TypeError.

    This doesn't exhaustively check all possible bad-args handling,
    but does try a couple of cases.
    """
    bad_fruit = {"orange": "two", "durian": 1}  # value you can't add
    not_a_dict = "What am I, chopped liver?"  # not even a dictionary
    combine_and_count(not_a_dict, bad_fruit)

test_bad_union()