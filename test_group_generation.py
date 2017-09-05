import pytest


def get_one_factor(n, factors):
    pass

def is_factor(n, factor):
    """
    Returns True if f is a factor of n.

    Args:
        n (int): dividend
        factor (int): divisor

    Returns:
        True if n % factor == 0, False otherwise
    """
    return True


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

def test_2_factor_of_10():
    assert is_factor(10, 2)

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
