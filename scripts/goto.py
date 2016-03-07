import click
from src.main import Main

@click.command()
@click.option('--add', default='')
def cli(add):
    if add != '':
        Main.goto(add)
