# terminal:
# initialization
git init

# master branch summary
git status

#
git add .

#
git commit -m "First commit for the project"  # if first time git will ask for user name # set up a check point, we can go back here from future

# 
git config --global user.email "xxx@gmail.com"
git config --global user.name "namexxx"

# changes on python main script
git status # will see modified main.py

# not in staged environment yet, to commit the change
git add main.py

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




