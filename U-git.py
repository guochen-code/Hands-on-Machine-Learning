**************************************************************************** initialization
# check current configuration
git config user.name
git config user.email

# create new configuration
git config --global user.name "user"
git config --global user.email "email"

# before try git init, check:
git status # make sure you not create a new init(repo) in an existing init(repo), no warming, but enventually will break

#initialization, use once per project
git init

# github - public vs private
# public
git clone https://github.com/guochen-code/my_second_repo.git
# private
git clone https://github.com/guochen-code/my_private_repo.git
#above command will not work, will show could not find the repo

# clone syntax with PAT: # go to developer setting in github and generate token
git clone https://<token@>github.com/guochen-code/my_private_repo.git

**************************************************************************** lcaol -- git add and git commit
git add file_one.txt file_two.txt
git commit -m "add file_one and file_two"
git add . # all all files in the directory
# press q button to quit the log view
**************************************************************************** github -- git remote and git push
git remote add origin https://github.com/guochen-code/my_second_repo.git # origin is default name by convention
# not everyone is allowed to upload files to github, need a token. so above origin will not work. correct command is:
git remote add origin https://<token@>github.com/guochen-code/my_second_repo.git
  
git remote remove origin # remove the origin
git remote -v # check what is the remote origin
git push -u origin master # push from local to github

**************************************************************************** git fetch and git pull (==git fetch and git merge)
# git fetch makes sense when you are working with others and not ready to override your own files in your local computer
# when you are travelling, you added a new file on github.
# when you back home, you want to see this files from your local machine through your IDE like pycharm instead ot web browser
git checkout origin/master # must have this origin in place # need to run git fetch prior to this command!!!!!!!!
# so correct steps will be:
git fetch
git checkout origin/master
# after above, you now are able to see the new file created on github. BUT NOTE up to now it didnot override your local working directory, you can just see it
# to undo, switch back to where we were
git switch master. # failed in my case, we can discard this new file by running: git checkout github_file.txt and then switch back to master and then can pull

# alternatively
git pull

**************************************************************************** git branch: create/switch/delete
git branch <my_branch_name>
git switch <my_branch_new>

git branch -d <my_branch_name> # use this one, because it will alert you if this branch is not merged before deleting it
git branch -D <my_branch_name> # will be forced to delete

**************************************************************************** merge
# fast forward merge: why fast forward? master have no commits, all the commits happened in the new_branch
# multiple branch commit merge with no conflict: if starting point the same, then create a new file in new branch, create a new file in master, merge, no conflict
# multiple branch commit merger with a conflict

# first to be on master branch
git merge <my_branch_name> # if with conflict, need to solve before auto merge can be executed. use PROPER editor to solve the conflict!!!!!!!!

**************************************************************************** git diff
# check your current files vs your latest commiited files
# when you make some changes but have not committed, you go away and come back from a coffee break, you don't remember what you did. 
# use: (this is in the same branch)
git diff

# how to use git diff for different branches?
git diff <branch_1> <branch_2>


**************************************************************************** git checkout: just go back and view the old files, not change anything
# easier way to find hash instead of use git log
git log --oneline

git checkout <hash_number>

# how to undo
git checkout master # go back to master and latest commit

**************************************************************************** undoing: git restore
# git restore filename # you change the file but not commit, use restore
# git restore --source HEAD~N filename # if you at 3rd commit, N=2 means you go back to the 1st commit
# git restore --staged filename # after execute git add filename, you want to revoke this action

**************************************************************************** undoing: git reset
# you just reset the commit, the news files still there!!!!!!!!!!
# this is useful if you accidentally committed to the wrong branch (for example, maybe you forgot to
# run git switch right after creating a new branch, accidentally committing to the original branch).
git reset <hash>

# what if you want the files to change:
git reset <hash> --hard

# application - mistakely commit on main branch, which is not supposed to be
(1) you have multiple commits 1-6
(2) you go and checkout commit 4
(3) you make some changes on code
(4) you find you did not switch to a new branch
(5) git reset to commit 4
(6) switch to the new branch
(7) add and commit in new branch



# git reset goes back and removes the commits and (changes files if its --hard)

**************************************************************************** undoing: git revert (encourage to use git revert over git reset whenever you can)
# imagine sb just created a branch off of one of the comnits we just got rid of, you can lose shared history !!!!!!
# this makes merge branches harder, definitely not impossible.
# git revert not change he project history, safe for commits that have already been published to a shared repo
# git revert creates a new commit that matches the historical state of previous commit
# git revert is a safer alternative to git reset in regards to losing work !!!!!!!!!

git revert <hash> # the code will be gone under the hash, but the commit hash still in the log!!!!!!!!!!!!!!!
# log if revert commit 2:
'''
commit-4 revert buggy commit # this is a new commit created !!!!!! so this state matches with commit-1 before buggy commit
commit-3
commit-2 buggy commit
commit-1
'''

**************************************************************************** git stash
# case context:
# when you are working on sth, on a new branch, not finished. you boss wants you to quickly switch to master branch to check sth.
# if you switch to the master, these changes will go along with you to the master, although not committed, but you can see them, not what we want
# so we want to stash these changes into a box, and reuse them later, when we back to the new branch from the master

# so in the new branch
git stash

# when you back to the new branch, you want these things back
(1) git stash pop # normal use case, they will be back
(2) git stash apply # memory fuzzy, you want them to be referred, not lose them.

