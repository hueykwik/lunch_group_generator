import click

from groups import make_groups

ROSTER_FILE = 'roster.txt'
ABSENT_FILE = 'absent.txt'

absent_nums = list()


@click.group()
def cli():
    """Makes lunch groups."""
    pass


@click.command()
@click.option('--name', prompt=True)
def add(name):
    """Add a name to the lunch roster."""
    with open(ROSTER_FILE, 'a') as f:
        f.write(name + '\n')
        click.echo('Addded %s to the lunch roster.' % name)


@click.command()
def clear():
    """Clear the lunch roster."""
    open(ROSTER_FILE, 'w').close()
    click.echo('Cleared the lunch roster')


def show_roster(roster):
    for i, name in enumerate(roster):
        click.echo("%d: %s" % ((i + 1), name))


def save_absent(row_nums, roster):
    with open(ABSENT_FILE, 'a') as f:
        for row_num in row_nums:
            f.write(roster[row_num] + '\n')


def prompt_row_number(roster_size):
    """Prompts the user for a row number in our roster, and checks that it is valid. If invalid, then prompts the user until a valid input is given. 0 is reserved for letting the user mark that they are done.
    """

    while True:
        row_num = click.prompt('Enter the id of the person who is absent (or 0 to stop)', type=int)

        if row_num <= roster_size:
            return row_num

        click.echo("Invalid id. Please try again.")


@click.command()
def absent():
    """Mark a person as absent."""
    roster = get_roster()
    show_roster(roster)

    roster_size = len(roster)
    while True:
        row_num = prompt_row_number(roster_size)
        if row_num == 0:
            break
        click.echo("Removed %s" % roster[row_num - 1])
        absent_nums.append(row_num - 1)

    save_absent(absent_nums, roster)


def filter_absent(roster):
    try:
        with open(ABSENT_FILE) as f:
            absent_names = f.read().splitlines()
    except FileNotFoundError:
        absent_names = set()

    absent_set = set(absent_names)

    return set(roster).difference(absent_set)


def get_roster(should_filter_absent=False):
    roster = []
    try:
        with open(ROSTER_FILE) as f:
            roster = f.read().splitlines()
    except FileNotFoundError:
        pass

    if should_filter_absent:
        roster = filter_absent(roster)

    return roster


@click.command()
def groups():
    """Generate groups for lunch."""
    roster = get_roster(True)

    if len(roster) < 3:
        click.echo("Roster is currently less than three people. Please use the add command to add more folks.")
        return

    group_list = make_groups(roster)

    click.echo("\nLunch Groups")
    click.echo("------------")
    for i, group in enumerate(group_list):
        group_label = 'Group %d: ' % (i + 1)
        click.echo(group_label + ', '.join(group))

cli.add_command(add)
cli.add_command(groups)
cli.add_command(clear)
cli.add_command(absent)

if __name__ == '__main__':
    cli()
