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
    click.echo('Clear the lunch roster')

def get_roster():
    roster = None
    with open(ROSTER_FILE) as f:
        roster = f.read().splitlines()
    return roster

@click.command()
def groups():
    """Generate groups for lunch."""
    roster = get_roster()

    group_list = make_groups(roster)

    for i, group in enumerate(group_list):
        group_label = 'Group %d: ' % (i+1)
        click.echo(group_label + ', '.join(group))

cli.add_command(add)
cli.add_command(groups)

if __name__ == '__main__':
    cli()

