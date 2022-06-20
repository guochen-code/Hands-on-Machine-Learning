git add : add to staging environment
git commit : commit the changes
******************************************************************** Part I ********************************************************************

# terminal:
# initialization
git init

# master branch summary
git status

# add into our staging environment
git add .

# once we add new directories or files to our staging environment, we have to commit these changes:
git commit -m "First commit for the project"  # if first time git will ask for user name # set up a check point, we can go back here from future

# if first time user, need to configure sth:
git config --global user.email "xxx@gmail.com"
git config --global user.name "namexxx"

# changes on python main script
git status # will see modified main.py

# not in staged environment yet, to commit the change 
git add main.py # git add . means all files, this time just specify the main.py file.

# 
git log # see previous commits, each has unique ID, press Q to quit

# go back to the previous commit time with ID being ID
git checkout <ID> # click main.py script, changes on the script (e.g. new functions) will be gone.

# 
git log # will only show commits up to the used <ID>, any commits after that will be gone

#
git checkout - # go to the master branch
# click main.py, we can see our new functions back
# git log, we can see our disappeared commits back ## press Q to quit


******************************************************************** Part II ********************************************************************
# check branches and current branch
git branch

# create a new branch
git branch <branch name>

# go to new branch
git checkout <branch name>

# now in the new branch and can make changes. after changes:
git add .
git commit -m "add xxx new functions"

# check 
git log # press Q to quit

# go back to master branch
git checkout master

# merge new branch to master branch
git merge <new branch name>

# create a new branch and checkout for you
git switch -c <new branch name>

# delete branch after merge
git branch -d <branch name>





