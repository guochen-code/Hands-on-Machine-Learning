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

######
pip freeze # show all installed dependencies

###### in terminal:
pip install -r requirements.txt

# requirements.txt example:
alembic==1.7.7
aiofiles==0.5.0
bcrypt==3.2.0
cffi==1.15.0
click==7.1.2
cryptography==35.0.0
ecdsa==0.17.0
fastapi==0.68.1
greenlet==1.1.2
h11==0.13.0
Jinja2==3.0.3
MarkupSafe==2.1.0
passlib==1.7.4
psycopg2-binary==2.9.3
pyasn1==0.4.8
pycparser==2.21
pydantic==1.9.0
PyMySQL==1.0.2
python-jose==3.3.0
python-multipart==0.0.5
rsa==4.8
six==1.16.0
SQLAlchemy==1.4.25
starlette==0.14.2
typing_extensions==4.1.1
uvicorn==0.13.4


******************************************************************************************************************************************************
# use another a new_requirements.txt to read requirements.txt
# content in the new_requirements.txt like:
-r requirements.txt
pytest>=6.2.3,<6.3.0
