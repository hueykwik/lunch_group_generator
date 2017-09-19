from click.testing import CliRunner

import lunch

SIX_PERSON = ['Huey', 'Dewey', 'Louie', 'Webby', 'Donald', 'Scrooge']

ELEVEN_PERSON = ['Grumpy', 'Sassy', 'Wimpy', 'Frowny', 'Silly', 'Hungry', 'Dopey', 'Snowy', 'Achy', 'Groany', 'Sickly']


def test_empty_roster():
    runner = CliRunner()

    with runner.isolated_filesystem():
        result = runner.invoke(lunch.cli, ['groups'])

        assert result.exit_code == 0
        assert 'Roster is currently less than three people' in result.output


def test_groups():
    runner = CliRunner()

    roster = SIX_PERSON

    with runner.isolated_filesystem():
        with open(lunch.ROSTER_FILE, 'w') as f:
            for person in roster:
                f.write("%s\n" % person)

        result = runner.invoke(lunch.cli, ['groups'])

        assert result.exit_code == 0
        assert 'Group 1' in result.output
        assert 'Group 2' in result.output


def test_add():
    runner = CliRunner()

    with runner.isolated_filesystem():
        result = runner.invoke(lunch.cli, ['add'], input='huey')

        assert result.exit_code == 0
        assert 'huey' in result.output


def test_add_groups():
    runner = CliRunner()

    with runner.isolated_filesystem():
        roster = SIX_PERSON
        for person in roster:
            result = runner.invoke(lunch.cli, ['add'], input=person)

        result = runner.invoke(lunch.cli, ['groups'])

        assert result.exit_code == 0
        assert 'Group 1' in result.output
        assert 'Group 2' in result.output


def test_mark_absent_out_of_bounds():
    runner = CliRunner()

    roster = ELEVEN_PERSON

    with runner.isolated_filesystem():
        with open(lunch.ROSTER_FILE, 'w') as f:
            for person in roster:
                f.write("%s\n" % person)

        result = runner.invoke(lunch.cli, ['absent'], input='12\n0')

        assert result.exit_code == 0
        print(result.output)
        assert 'Invalid id' in result.output


def test_mark_absent():
    runner = CliRunner()

    roster = ELEVEN_PERSON

    with runner.isolated_filesystem():
        with open(lunch.ROSTER_FILE, 'w') as f:
            for person in roster:
                f.write("%s\n" % person)

        result = runner.invoke(lunch.cli, ['absent'], input='1\n0')
        assert 'Removed Grumpy' in result.output

        assert result.exit_code == 0


def test_all_absent():
    runner = CliRunner()

    roster = ELEVEN_PERSON

    with runner.isolated_filesystem():
        with open(lunch.ROSTER_FILE, 'w') as f:
            for person in roster:
                f.write("%s\n" % person)

        with open(lunch.ABSENT_FILE, 'w') as f:
            for person in roster:
                f.write("%s\n" % person)

        result = runner.invoke(lunch.cli, ['groups'])
        assert result.exit_code == 0
        assert 'Roster is currently less than three people' in result.output


def test_eleven_two_absent():
    runner = CliRunner()

    roster = ELEVEN_PERSON
    absentees = ['Achy', 'Sickly']

    with runner.isolated_filesystem():
        with open(lunch.ROSTER_FILE, 'w') as f:
            for person in roster:
                f.write("%s\n" % person)

        with open(lunch.ABSENT_FILE, 'w') as f:
            for person in absentees:
                f.write("%s\n" % person)

        result = runner.invoke(lunch.cli, ['groups'])
        assert 'Group 1' in result.output
        assert 'Group 2' in result.output
