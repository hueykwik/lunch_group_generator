import click

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

# @click.command()
# def make_groups():
#     print("Making Groups")

if __name__ == '__main__':
    cli()
