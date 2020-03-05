#!/usr/bin/env python

import click
import os
import json

@click.group()
def author():
    """
    Welcome to author, an easy way to configure your git
    """

@click.option('-n', '--name', help="Use this name, jumping name option")
@click.option('-e', '--email', help="Use this email, jumping email option")
@click.option('-u', '--user', help="Use this user, jumping name option")
@author.command(help="create a new user")
def add(name: str, email: str, user: str):
    user_data = {'name':'', 'email':''}
    if name == None:
        user_data['name'] = input("Name >> ")
    else:
        user_data['name'] = name

    if email == None:
        user_data['email'] = input("Email >> ")
    else:
        user_data['email'] = email

    if user == None:
        user_filename = input("User >> ")
    else:
        user_filename = user

    filename = os.path.join(os.path.expanduser('~'),'.config/author',user_filename+'.json')
    json.dumps(user_data)

    with open(filename,'w') as archive:
        json.dump(user_data, archive)


@click.option('-g', '--change-global', is_flag=True, help="change the global config file")
@click.argument('user')
@author.command(help="change git user")
def change(change_global: bool, user: str):
    filename = os.path.join(os.path.expanduser('~'),'.config/author',user+'.json')
    try:
        with open(filename, 'r') as archive:
            user_data = json.load(archive)
            if change_global:
                os.system("git config --global user.name '"+ user_data['name'] +"'")
                os.system("git config --global user.email '" + user_data['email'] + "'")
            else:
                os.system("git config user.name '" + user_data['name'] + "'")
                os.system("git config user.email '" + user_data['email'] + "'")
    except:
        print("This user don't exist")






if __name__ == '__main__':
    author(prog_name='author')
