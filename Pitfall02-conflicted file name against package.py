Traceback (most recent call last):
  File "C:\Users\CGuo\PycharmProjects\pythonProject\1+1.py", line 1, in <module>
    import requests
  File "C:\Users\CGuo\PycharmProjects\pythonProject\venv\lib\site-packages\requests\__init__.py", line 43, in <module>
    import urllib3
  File "C:\Users\CGuo\PycharmProjects\pythonProject\venv\lib\site-packages\urllib3\__init__.py", line 11, in <module>
    from . import exceptions
  File "C:\Users\CGuo\PycharmProjects\pythonProject\venv\lib\site-packages\urllib3\exceptions.py", line 3, in <module>
    from .packages.six.moves.http_client import IncompleteRead as httplib_IncompleteRead
  File "C:\Users\CGuo\PycharmProjects\pythonProject\venv\lib\site-packages\urllib3\packages\six.py", line 234, in create_module
    return self.load_module(spec.name)
  File "C:\Users\CGuo\PycharmProjects\pythonProject\venv\lib\site-packages\urllib3\packages\six.py", line 209, in load_module
    mod = mod._resolve()
  File "C:\Users\CGuo\PycharmProjects\pythonProject\venv\lib\site-packages\urllib3\packages\six.py", line 118, in _resolve
    return _import_module(self.mod)
  File "C:\Users\CGuo\PycharmProjects\pythonProject\venv\lib\site-packages\urllib3\packages\six.py", line 87, in _import_module
    __import__(name)
  File "C:\Users\CGuo\AppData\Local\Programs\Python\Python39\lib\http\client.py", line 71, in <module>
    import email.parser
ModuleNotFoundError: No module named 'email.parser'; 'email' is not a package

Process finished with exit code 1

# email.py is the root cause. rename the script because it conflicted with module in requests. 
# so whenever there is requests in a script, this script will fail and trigger emai.py and that's why keep receiving emails.
