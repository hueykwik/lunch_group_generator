import pytest

from groups import *

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

    with pytest.raises(ValueError):
        get_group_sizes(None)

    with pytest.raises(ValueError):
        get_group_sizes(-1)

    with pytest.raises(ValueError):
        get_group_sizes(2)

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
    group_members = [member for group in new_groups for member in group]
    assert len(original_members) == len(group_members)
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

def test_team_of_206():
    team = ['Name%d' % i for i in range(206)]
    groups = make_groups(team)

    assert len(groups) == 68
    assert membership_equal(team, groups)
