#! /usr/bin/python3

import os

def run():
    print("Hello welcome to dotnet ef add migration script\n to exit just press Ctrl-C")

    name = input('Enter migration name: ')
    context = input('Enter context name: ')
    project = input('Enter project name: ')
    startup = input('Enter startup name: ')
    command = f"dotnet ef migrations add {name} --context {context} --project {project} --startup-project {startup}"

    want_output_folder = input('Do you want output folder for migrations? [y/n]: ')

    if want_output_folder == 'y':
        output = input('Enter output: ')
        command += "-o {output}"    

    os.system(command)
    exit()


while True:
    run()
