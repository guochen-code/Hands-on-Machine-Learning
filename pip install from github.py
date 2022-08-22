# (1) make sure it has setup.py
# (2) create a virtual environment:
python -m venv env
source env/bin/activate
#(3) install from github 
pip install -e git+https://github.com/pallets/flask#egg=flask
  # -e: editable
  # ##egg=flask: when you use -e you have to supply a name, just name of the library that you are installing

pip freeze -> -e git+https://github.com/pallets/flask@4e854XXXXXXXXXXXXXXXXXXXXXX#egg=Falsk

pip uninstall flask

# ****************************************************** want to install older version from git
# (1) on github: dropdown menu - tag - find older version
# (2) install from github
pip install git+https://github.com/pallets/flask@0.5
  
pip freeze -> Flask ==0.5.dev20200710


****************************************************************************************************************************************
# How to pip install from a git repository
# If this is a new repo, you'll minimally need a setup.py so that pip can carry out the install. 
# Other than that, it really just boils down to giving pip a git repository URL.

# You can explicitly call out the package name that you're installing with #egg=
# The syntax
pip install git+<repository_url>#egg=<package_name>
# Explicit package name example
pip install git+https://github.com/matiascodesal/git-for-pip-example.git#egg=git-for-pip-example
  
# There are also a number of different ways to specify a version of the repository that you want to fetch. 
# It's wise to use one of these methods to lock your dependency so that you get consistent results.
# Use a commit SHA
pip install git+https://github.com/matiascodesal/git-for-pip-example.git@4045597#egg=git-for-pip-example
# Use a tag
pip install git+https://github.com/matiascodesal/git-for-pip-example.git@v1.0.0#egg=git-for-pip-example
# Use a branch called "GreetingArg"
pip install git+https://github.com/matiascodesal/git-for-pip-example.git@GreetingArg#egg=git-for-pip-example
  
# How to include the dependency in a requirements.txt
# If a git repository dependency is going to live in a project for more than just testing, you'll likely want to add it to your requirements.txt. 
# There's a bug with "pip freeze" where the git repository dependency wasn't being output by "pip freeze". That was only recently fixed in pip 20.1. 
# I'll show you the workaround for older versions of pip and the new way to list the dependency. 
# The workaround for older versions of pip is to use the -e or --editable flag:
# The pip command with "-e"
pip install -e git+https://github.com/matiascodesal/git-for-pip-example.git@v1.0.0#egg=my-git-package

# What that should look like in your requirements.txt
packageA==1.2.3
-e https://github.com/matiascodesal/git-for-pip-example.git@v1.0.0#egg=my-git-package
packageB==4.5.6

# For pip 20.1 or newer, you no longer need the -e flag:
# Just put the pip install argument straight into your requirements.txt
packageA==1.2.3
git+https://github.com/matiascodesal/git-for-pip-example.git@v1.0.0#egg=my-git-package
packageB==4.5.6

# Or you can use the preferred PEP 440 direct URL syntax
packageA==1.2.3
git-for-pip-example @ git+https://github.com/matiascodesal/git-for-pip-example.git@v1.0.0
packageB==4.5.6
