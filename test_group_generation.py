import pytest

def divisible_by(dividend, divisors):
    """
    Returns a divisor that can divide dividend without a remainder, or None.

    Args:
        dividend(int):
        divisors(list): A list of divisors, i.e. integers to divide by

    Returns:
        A divisor that can divide dividend without a remainder, otherwise None.
        If multiple divisors in `divisors` satisfy this criteria, this function
        will arbitrarily return one of them.
    """

def make_groups(people):
    """Makes groups from a list of people.

    Args:
        people(list): A list of people.

    Returns:
        A list of groups, where each group size is between 3 to 5, inclusive.

    Raises:
        ValueError: number of people is less than 3 or none.

    """
    if people is None or len(people) < 3:
        raise ValueError("Number of people should be at least 3")

    return [people]

def test_10_divisible_by_2():
    divisor = divisible_by(10, [2])
    assert divisor == 2

def test_empty_team():
    with pytest.raises(ValueError):
        make_groups(None)

def test_less_than_three_people():
    with pytest.raises(ValueError):
        make_groups(['Happy', 'Dopey'])

def test_team_of_four():
    team = ['Happy', 'Dopey', 'Grumpy', 'Sneezy']
    groups = make_groups(team)

    assert len(groups) == 1

def test_team_of_eight():
    team = ['Happy', 'Dopey', 'Grumpy', 'Sneezy', 'Bashful', 'Sleepy', 'Doc', 'Snow']
    groups = make_groups(team)

    assert len(groups) == 2
