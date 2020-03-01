#!/usr/bin/env python

import click
import os
import json

@click.group()
def author():
    """
    Welcome to author, an easy way to configure your git
    """

@author.command(help="create a new user")
def add():
    user_data = {'name':'', 'email':''}
    user_data['name'] = input("Name >> ")
    user_data['email'] = input("Email >> ")

    user_filename = input("User >> ")
    filename = os.path.join(os.path.expanduser('~'),'.config/author',user_filename+'.json')
    json.dumps(user_data)

    with open(filename,'w') as archive:
        json.dump(user_data, archive)


@click.argument('user')
@author.command(help="change git user")
def change(user: str):
    filename = os.path.join(os.path.expanduser('~'),'.config/author',user+'.json')
    try:
        with open(filename, 'r') as archive:
            user_data = json.load(archive)
            os.system("git config --global user.name '"+ user_data['name'] +"'")
            os.system("git config --global user.email '" + user_data['email'] + "'")
    except:
        print("This user don't exist")






if __name__ == '__main__':
    author(prog_name='author')
