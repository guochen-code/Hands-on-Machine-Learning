in terminal: (python for windows, python3 for mac) below for windows:
  
mkdir <main directory name> # make a new directory for a new project
cd <main directory name> # change directory to the new directory
pip list # check installed dependencies, especially look for whether virtualenv already installed (pip install virtualenv) if not
python -m venv <env name>
cd <env name>
cd Scripts
activate # activate the virtual env, notice the change in front of the terminal line (deactivate) to deactivate the virtual env
cd.. # go back one level
cd.. # go back another level, back to main directory
pip install fastapi[all] # install all dependencies for the fastapi

# go to pycharm
open - select main directory

************* *********** mac:
# create virtualenv
python3 -m venv <env name>
. <env name>/bin/activate

# to deactivate
cd <env name>
cd bin
$source deactivate

cd..
cd..

pip install fastapi[all] # install all dependencies for the fastapi




