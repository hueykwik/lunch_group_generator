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
        f.write(name)
        click.echo('Addded %s to the lunch roster.' % name)

@click.command()
def clear():
    """Clear the lunch roster."""
    open(ROSTER_FILE, 'w').close()
    click.echo('Cleared the lunch roster')

def get_roster():
    roster = None
    with open(ROSTER_FILE) as f:
        roster = f.read().splitlines()
    return roster

@click.command()
def groups():
    """Generate groups for lunch."""
    try:
        roster = get_roster()
    except FileNotFoundError:
        click.echo("Roster is currently empty. Please use the 'add' command to add people.")
        return

    group_list = make_groups(roster)

    click.echo("\nLunch Groups")
    click.echo("------------")
    for i, group in enumerate(group_list):
        group_label = 'Group %d: ' % (i+1)
        click.echo(group_label + ', '.join(group))

cli.add_command(add)
cli.add_command(groups)
cli.add_command(clear)

if __name__ == '__main__':
    cli()

