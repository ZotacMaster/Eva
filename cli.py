"""Defines all the terminal commands to be used by the agent
    Using the click module
"""

import click as c

@c.command()
@c.option('--start', default= True)

def start_server(start: bool)-> bool:
    pass