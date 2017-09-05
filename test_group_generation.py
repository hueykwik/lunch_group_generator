import pytest

from random import sample


def get_one_factor(n, possible_factors):
    """
    Returns one of the possible_factors if it is actually a factor of n,
    otherwise None.

    Args:
        n (int): dividend
        possible_factors (list): list of possible factors


    Returns:
        One of the possible_factors if it is a factor, None otherwise.
        If multiple values in possible_factors are factors, it returns the
        earliest value in the list of possible_factors.
    """
    for possible_factor in possible_factors:
        if is_factor(n, possible_factor):
            return possible_factor

    return None

def is_factor(n, factor):
    """
    Returns True if f is a factor of n.

    Args:
        n (int): dividend
        factor (int): divisor

    Returns:
        True if n % factor == 0, False otherwise
    """
    return n % factor == 0

def make_groups(people, group_sizes=[3,4,5]):
    """Makes groups from a list of people.

    Args:
        people(list): A list of people.
        group_sizes(list): A list of group sizes.

    Returns:
        A list of groups, where each group size is between 3 to 5, inclusive.

    Raises:
        ValueError: number of people is less than 3 or none.

    """

    if people is None or len(people) < 3:
        raise ValueError("Number of people should be at least 3")

    shuffled_people = sample(people, len(people))

    group_size = get_one_factor(len(people), group_sizes)
    start_index = 0

    num_groups = len(people) // group_size
    groups = list()

    for i in range(num_groups):
        group = shuffled_people[start_index:start_index+group_size]
        groups.append(group)

        start_index += group_size

    return groups

def test_get_one_factor():
    assert get_one_factor(12, [3,4,5]) == 3
    assert get_one_factor(12, [4,3,5]) == 4

def test_get_one_factor_no_factors():
    assert get_one_factor(29, [3,4,5]) == None

def test_10_factor_of_2():
    assert not is_factor(2, 10)

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

def membership_equal(original_team, new_groups):
    original_members = set(original_team)
    group_members = set([member for group in new_groups for member in group])

    return original_members == group_members

def test_team_of_eight():
    team = ['Happy', 'Dopey', 'Grumpy', 'Sneezy', 'Bashful', 'Sleepy', 'Doc', 'Snow']
    groups = make_groups(team)

    assert len(groups) == 2
    assert membership_equal(team, groups)

def test_team_of_nine():
    team = ['Happy', 'Dopey', 'Grumpy', 'Sneezy', 'Bashful', 'Sleepy', 'Doc', 'Snow', 'Clumsy']
    groups = make_groups(team)

    members = [member for group in groups for member in group]
    members = set(members)
    original_members = set(team)

    assert len(groups) == 3
    assert membership_equal(team, groups)

