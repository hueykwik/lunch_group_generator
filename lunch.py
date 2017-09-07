import click

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
    click.echo('Dropped the database')

cli.add_command(add)
cli.add_command(groups)

if __name__ == '__main__':
    cli()

