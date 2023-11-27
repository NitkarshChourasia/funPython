# Importing necessary modules
import os
from random import randint


# for i in range(1,(365*2)+1):

#     for j in range(0,randint(1,10000)):
#         d=str(i)+' days ago'
#         with open ('file.txt','a')as file:
#             file.write(d)
#         os.system('git add .')
#         os.system('git commit --date="'+d+'" -m "commit {}"'.format((randint(1,99999)))) # Should learn this thing (code line)
# os.system('git push -u origin main')
# Should Improve this program, such a lovely program it is..
# Make it, clean.
# Readability and documentation, and clean coding is the thing.

days_back = 365 * 2
commit_per_day = 10000
random = randint(1, 10000)  # Random number

# past day range.
for i in range(1, days_back + 1):
    # git commit range.

    for j in range(0, randint(1, 10000)):
        # changes to reflect for git commit to happen.
        d = str(i) + " days ago"

        with open("file.txt", "a") as file:
            file.write(d)

        os.system("git add .")
        os.system(
            'git commit --date="' + d + '" -m "commit {}"'.format((randint(1, 99999)))
        )  # Should learn this thing (code line)

os.system("git push -u origin main")
