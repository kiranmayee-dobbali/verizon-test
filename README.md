This is for verizon test.

# Verizon Random Number Generator:
This project is to generate a 4 digit random code based on current date,time and pi value.


## Steps to run the program:
This program is developed in python 3.8 version.
Once you are in Verizon folder, follow below steps:

``` bash
$ cd verizon
$ python runner.py
```

or
If your default version is not python 3 use:
``` bash
$ cd verizon
$ python3 runner.py
```
Example output:
``` bash
C:\Users\md\AppData\Local\Programs\Python\Python38\python.exe C:/Users/md/PycharmProjects/Verizon/verizon/runner.py
New 4 digit random code is : 2868
```
## Steps to run the unittest program:
``` bash
$ cd tests
$ python test_code_generator.py
```

Example output:
``` bash
Testing started at 9:17 PM ...
C:\Users\md\AppData\Local\Programs\Python\Python38\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 2019.3.1\plugins\python-ce\helpers\pycharm\_jb_unittest_runner.py" --path C:/Users/md/PycharmProjects/Verizon/tests/test_code_generator.py
Launching unittests with arguments python -m unittest C:/Users/md/PycharmProjects/Verizon/tests/test_code_generator.py in C:\Users\md\PycharmProjects\Verizon\tests

Ran 8 tests in 0.011s

OK
```
## Steps to access the documentation
``` bash
$ cd build
$ cd html
```
Open index.html in this folder.

### The resulting directory structure


The directory structure of project looks like this: 

```
├───build
│   ├───doctrees
│   └───html                               <- This folder contains index.html which has the documentation.
│       ├───_modules
│       │   └───verizon
│       ├───_sources
│       └───_static
├───source
│   ├───_static
│   └───_templates
├───tests                                  <- This folder contains test_code_generator module.
└───verizon                                <- This folder contains code_generator and runner modules.
    └───__pycache__
```



