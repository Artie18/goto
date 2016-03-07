import click
from src.main import Main
from src.keyword import Keyword
from click.testing import CliRunner
import sys, io
import subprocess

@click.command()
@click.argument('arg1', default='help')
@click.argument('arg2', nargs=-1)
def cli(arg1, arg2):
    subprocess.Popen('cd /Applications', shell=True, executable="/bin/zsh")
    # if len(arg2) > 1:
    #     keyword, path = arg2[0], arg2[1]
    # else:
    #     keyword, path = arg2[0], ''
    #
    # if arg1 != '':
    #     keywordClass = Keyword(arg1)
    #     result = Main.execute(keywordClass, keyword, path)
