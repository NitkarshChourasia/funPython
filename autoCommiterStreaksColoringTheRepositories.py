import os
from random import randint
for i in range(1,(365*2)+1):
    for j in range(0,randint(1,10000)):
        d=str(i)+' days ago'
        with open ('file.txt','a')as file:
            file.write(d)
        os.system('git add .')
        os.system('git commit --date="'+d+'" -m "commit {}"'.format((randint(1,99999)))) # Should learn this thing (code line)
os.system('git push -u origin main')
# For to Per day push just put it in 1st for loop, hehe.
# Should Improve this program, such a lovely program it is..
