import click

from groups import make_groups

ROSTER_FILE = 'roster.txt'


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


@click.command()
def absent():
    """Mark a person as absent."""
    roster = get_roster()
    show_roster(roster)

    absent_nums = list()

    row_num = click.prompt('Enter the id of the person who is absent', type=int)

    absent_nums.append(row_num)




def get_roster():
    roster = []
    try:
        with open(ROSTER_FILE) as f:
            roster = f.read().splitlines()
    except FileNotFoundError:
        pass

    return roster


@click.command()
def groups():
    """Generate groups for lunch."""
    roster = get_roster()

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

