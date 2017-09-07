import click
from click.testing import CliRunner

import lunch

def test_groups():
    runner = CliRunner()

    roster = ['Huey', 'Dewey', 'Louie', 'Webby', 'Donald', 'Scrooge']

    with runner.isolated_filesystem():
        with open(lunch.ROSTER_FILE, 'w') as f:
            for person in roster:
                f.write("%s\n" % person)

        result = runner.invoke(lunch.cli, ['groups'])

        assert result.exit_code == 0
        assert 'Group 1' in result.output
        assert 'Group 2' in result.output
