import click

from groups import make_groups

roster = ['Happy', 'Dopey', 'Grumpy', 'Sneezy', 'Bashful', 'Sleepy', 'Doc', 'Snow', 'Clumsy', 'Wishy-Washy', 'Coughy']

@click.group()
def cli():
    """Makes lunch groups."""
    pass

@click.command()
def add():
    """Add people to the lunch roster."""
    click.echo('Add a person or persons to the lunch roster')

@click.command()
def groups():
    """Generate groups for lunch."""
    group_list = make_groups(roster)

    for i, group in enumerate(group_list):
        group_label = 'Group %d: ' % (i+1)
        click.echo(group_label + ', '.join(group))

cli.add_command(add)
cli.add_command(groups)

if __name__ == '__main__':
    cli()

