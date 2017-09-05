import pytest

from random import sample

GROUP_SIZES = [3,4,5]

def get_group_sizes(n):
    """
    Given a number n, returns the group sizes needed to split the group
    mostly evenly.

    Some values of n do not divide evenly by a single group size of 3, 4, or 5.
    In that case, we return two group sizes:

    1. Special group size: One group will have this size.
    2. Normal group size: The rest of the groups will have this size.

    An example makes this clearer:

    Let n = 11 and group sizes are 3, 4, and 5. These group sizes are not factors of 11.

    However, if we make a group of 3, then we can split the remaining members into groups of 4. `special_group_size` would then be 3, and `group_size` would be 4.

    Args:
        n (int): number of members
        group_sizes(list): list of possible group_sizes

    Returns:
        Group size and a special group size. If there is no special group size, then it will have a value of None.
    """
    group_size = get_one_factor(n, GROUP_SIZES)
    special_group_size = None

    if group_size is not None:
        return group_size, None

    for size in GROUP_SIZES:
        group_size = get_one_factor(n-size, GROUP_SIZES)
        if group_size:
            special_group_size = size
            break

    return group_size, special_group_size

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

    num_people = len(people)

    shuffled_people = sample(people, num_people)

    groups = list()
    start_index = 0

    group_size, special_group_size = get_group_sizes(num_people)

    #group_size = get_one_factor(num_people, GROUP_SIZES)

    # if group_size is None:
    #     diff_group_size = get_diff_group_size(num_people, group_sizes)

    #     num_people -= len(diff_group) # Fix this


    num_groups = num_people // group_size

    # if needed, add a group that's not the same as group_size

    for i in range(num_groups):
        group = shuffled_people[start_index:start_index+group_size]
        groups.append(group)

        start_index += group_size

    return groups

def test_get_group_sizes():
    group_size, special_group_size = get_group_sizes(12)
    assert group_size == 3
    assert special_group_size == None

    group_size, special_group_size = get_group_sizes(8)
    assert group_size == 4
    assert special_group_size == None

    group_size, special_group_size = get_group_sizes(11)
    assert group_size == 4
    assert special_group_size == 3

    group_size, special_group_size = get_group_sizes(98)
    assert group_size == 5
    assert special_group_size == 3

    group_size, special_group_size = get_group_sizes(997)
    assert group_size == 3
    assert special_group_size == 4

def test_special_group_sizes():
    n_values = [x for x in range(3,1000) if x%3 and x%4 and x%5]

    for n in n_values:
        group_size, special_group_size = get_group_sizes(n)
        assert group_size in GROUP_SIZES
        assert special_group_size in GROUP_SIZES


def test_get_one_factor():
    assert get_one_factor(12, GROUP_SIZES) == 3
    assert get_one_factor(12, [4,3,5]) == 4

def test_get_one_factor_no_factors():
    assert get_one_factor(29, GROUP_SIZES) == None

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

    assert len(groups) == 3
    assert membership_equal(team, groups)

def test_team_of_eleven():
    team = ['Happy', 'Dopey', 'Grumpy', 'Sneezy', 'Bashful', 'Sleepy', 'Doc', 'Snow', 'Clumsy', 'Wishy-Washy', 'Coughy']
    groups = make_groups(team)

    assert len(groups) == 3
    assert membership_equal(team, groups)

