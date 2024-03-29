# 0x01-shell_permissions

## Learning Objectives
- What do the commands chmod, sudo, su, chown, chgrp do
- Linux file permissions
- How to represent each of the three sets of permissions (owner, group, and other) as a single digit
- How to change permissions, owner and group of a file
- Why can’t a normal user chown a file
- How to run a command with root privileges
- How to change user ID or become superuser
- How to create a user
- How to create a group
- How to print real and effective user and group IDs
- How to print the groups a user is in
- How to print the effective userid

## Task/File Descriptions

- Script0 - Changes your user ID to betty.
- Script1 - Prints the effective userid of the current user.
- Script2 - Prints all the groups the current user is part of.
- Script3 - Changes the owner of the file hello to the user betty.
- Script4 - Creates an empty file called hello.
- Script5 - Adds execute permission to the owner of the file hello.
- Script6 - Adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
- Script7 - Adds execution permission to the owner, the group owner and the other users, to the file hello.
- Script8 - Sets the permission to the file hello as ------rwx
- Script9 - Sets the mode of the file hello to: -rwxr-x-wx
- Script10 - Sets the mode of the file hello the same as ollehs mode.
- Script11 - Adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.
- Script12 - Creates a directory called dir(underscore)holberton with permissions 751 in the working directory.
- Script13 - Changes the group owner to holberton for the file hello.
- Script14 - Changes the owner to betty and the group owner to holberton for all the files and directories in the working directory.
- Script15 - changes the owner and the group owner of the file (underscore)hello to betty and holberton respectively.
- Script16 - Changes the owner of the file hello to betty only if it is owned by the user guillaume.
- Script100 - Play StarWars IV
