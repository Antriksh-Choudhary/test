import os
from datetime import date, time, datetime
import datetime
from random import randint as ri

total_day = 1  # how far back to start commits
commit_freq = 50  # num of commits per day

# set to True if you want the number of commits per day to be random for a more realistic graph
variablity = True

# change to your repo
# repo_link = "git@github.com:aliifam/github-activity-generator.git" # ssh
repo_link = "https: // github.com/Antriksh-Choudhary/test.git"  # http

tl = total_day  # time day
ctr = 1
ct = commit_freq

now = datetime.datetime.now()

f = open("commit.txt", "w")
os.system("git config user.name")
os.system("git config user.email")
os.system("git init")

pointer = 0

while tl > 0:
    if variablity:
        # variable number of commits per day so your graph isn't suspicously the same color throughout
        ct = ri(0, commit_freq + 1)

    while ct > 0:
        f = open("commit.txt", "a+")
        l_date = now + datetime.timedelta(days=-pointer)
        formatdate = l_date.strftime("%Y-%m-%d")
        f.write(f"commit ke {ctr}: {formatdate}\n")
        f.close()
        os.system("git add .")
        os.system(
            f"git commit --date=\"{formatdate} 12:15:10\" -m \"commit ke {ctr}\"")
        print(f"commit ke {ctr}: {formatdate}")
        ct -= 1
        ctr += 1
    pointer += 1
    tl -= 1

os.system(f"git remote add origin {repo_link}")
os.system("git branch -M main")
os.system("git push -u origin main -f")
