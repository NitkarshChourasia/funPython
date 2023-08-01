import os
import random

def test():
    counter = 0
    while counter < 10:
        command = "echo Hello{0} >> test.txt".format(int((random.random())*(random.randint(1,1000))))
        os.system(command)
        counter = counter + 1

def gitPush():
    # Creating the command variables.

    add = "git add --all"
    commit = 'git commit -S -m "newCommits @ `date +%F-%T`"'
    push = "git push"
    fetch = "git fetch"
    pull = "git pull"

    # Executing the commands.
    os.system(add)
    os.system(commit)
    os.system(push)
    os.system(fetch)
    os.system(pull)

gitPush()
