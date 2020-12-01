# 1. How to check status of aNANt-dev (with server access)

This document contains instructions on checking the current status of development of aNANt. 
It is assumed here that you have access to the aNANt server.

1. `ssh` into the aNANt server. The LAN address is `abhishek@10.98.24.89`. Go to the `aNANt-dev` folder.

2. Run `sync.sh` script. This will bring the local clone up to date with all the remote branches.

3. Run `git branch -r` to get a list of the different branches.

4. To select your required branch, type `git checkout <branch-name>`

5. Run `python manage.py runserver 0.0.0.0:8080`, this will deploy a django server at port 8080. Check FAQ in README.md if you have any problems.

6. Type `10.98.24.89:8080/` in your browser. You should be connected to the local network. 

